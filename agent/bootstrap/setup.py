from pathlib import Path

from urllib.parse import urlparse

import httpx

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.status import Status
from rich.table import Table
from rich.live import Live
from rich.spinner import Spinner

from decouple import config

from api.client import BasicClient

from config.config import Settings, load_settings

from services.hardware_parser import ProductionParser

from services.utils import get_os_info, get_public_ip_native, get_system_hostname

console = Console()

BASE_DIR = Path(__file__).resolve().parents[1]
ENV_FILE = BASE_DIR / ".env"


def render_header() -> None:
    """
    Print the entrance header.
    """

    console.print(
        Panel.fit(
            "\n"
            "[bold cyan]NexoraControl Agent Setup[/bold cyan]\n"
            "[dim]Connect this machine to your NexoraControl server.[/dim]\n",
            title="NexoraControl",
            border_style="cyan",
            padding=(0, 2),
        )
    )


def render_step(
    number: int,
    total: int,
    title: str,
    description: str = "",
) -> None:
    """
    Print information about the step, including its description, title, number of step and total step value.

    Args:
        number (int): number of step.
        total (int): the total number of steps.
        title (str): title of step.
        description (str, optional): description of step. Defaults to "".
    """

    console.print(
        f"\n[bold cyan]Step {number} of {total}[/bold cyan] "
        f"[dim]—[/dim] [bold]{title}[/bold]\n"
    )

    if description:
        console.print(f"[dim]{description}[/dim]\n")


def clear_and_render() -> None:
    """
    Clear the terminal screen and render the application header.

    This function acts as equivalent of the 'cls' on Windows or 'clear' on Linux, then displays the header.
    """

    console.clear()
    render_header()


def is_valid_api_url(url: str) -> bool:
    """
    Check if the URL is valid and return True if it is correct.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL has a valid scheme and network location, False otherwise.
    """
    try:
        parsed = urlparse(url)

        return parsed.scheme in {"http", "https"} and bool(parsed.netloc)
    except ValueError:
        return False


def save_config(
    api_url: str,
    agent_id: int,
    token: str,
    heartbeat_interval: int,
    command_interval: int,
) -> None:
    """
    Save the passed arguments into the .env file.

    Args:
        api_url (str): The backend API URL.
        agent_id (int): The agent ID.
        token (str): The secret UUID token.
        heartbeat_interval (int): The interval in seconds between heartbeat requests.
        command_interval (int): The interval in seconds between command requests.
    """
    ENV_FILE.write_text(
        "\n".join(
            [
                f"NEXORA_API_URL={api_url}",
                f"NEXORA_AGENT_ID={agent_id}",
                f"NEXORA_TOKEN={token}",
                f"NEXORA_HEARTBEAT_INTERVAL={heartbeat_interval}",
                f"NEXORA_COMMAND_INTERVAL={command_interval}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    ENV_FILE.chmod(0o600)


def show_error(title: str, description: str) -> None:
    """
    Print an error message with title and description.

    Args:
        title (str): The title of error.
        description (str): The description of error.
    """
    console.print(
        Panel(
            f"[bold red]✗ {title}[/bold red]\n\n" f"[dim]{description}[/dim]",
            border_style="red",
            padding=(1, 2),
        )
    )


def show_success(title: str, description: str) -> None:
    """
    Print a success message with title and description.

    Args:
        title (str): The title of message.
        description (str): The description of message.
    """
    console.print(
        Panel(
            f"[bold green]✓ {title}[/bold green]\n\n" f"{description}",
            border_style="green",
            padding=(1, 2),
        )
    )


def show_configuration(
    api_url: str,
    agent_id: int,
    hostname: str,
    name: str,
) -> None:
    """
    Print the configuration styled like table with passed arguments.

    Args:
        api_url (str): The backend API URL.
        agent_id (int): The agent ID.
        hostname (str): The agent hostname.
        name (str): The agent name.
    """
    table = Table(
        title="Agent configuration",
        border_style="green",
        title_style="bold green",
    )

    table.add_column("Property", style="bold")
    table.add_column("Value", style="cyan")

    table.add_row("Machine name", name)
    table.add_row("Hostname", hostname)
    table.add_row("Agent ID", str(agent_id))
    table.add_row("API URL", api_url)

    console.print(table)


async def request_with_live_spinner(
    client: BasicClient, method: str, payload: dict
) -> dict | None:
    spinner = Spinner("dots", text="[cyan]Connecting to NexoraControl API...[/cyan]")

    with Live(spinner, console=console, refresh_per_second=10, transient=True):
        try:
            client_func = getattr(client, method)

            response, status_code = await client_func(payload)

            if status_code != 201:
                detail = "The server rejected the request."

                if response:
                    detail = response.get(
                        "detail",
                        "The server rejected the request.",
                    )

                show_error(
                    "Registration failed",
                    f"HTTP status: {status_code}\n" f"Reason: {detail}",
                )
                return None

            return response, status_code

        except httpx.ConnectError:
            show_error(
                "Connection failed",
                "Unable to connect to the NexoraControl API.\n\n"
                "Check the API URL and make sure the server is reachable.",
            )
            return None

        except httpx.TimeoutException:
            show_error(
                "Request timed out",
                "The NexoraControl API did not respond in time.",
            )
            return None

        except httpx.HTTPError as exc:
            show_error(
                "HTTP error",
                str(exc),
            )
            return None

        except Exception as exc:
            show_error(
                "Unexpected error",
                f"{type(exc).__name__}: {exc}",
            )
            return None


async def setup_agent(force: bool = False) -> Settings | None:
    """
    The main function to set up the agent.

    Returns:
        Settings | None: The Settings object if the configuration already exists,
        None otherwise.
    """
    settings = load_settings()

    if not force:
        if settings.agent_id and settings.token:
            return settings

    # ============================================================
    # STEP 1 — API
    # ============================================================

    clear_and_render()

    render_step(
        1,
        3,
        "Server connection",
        "Tell NexoraControl where your server API is located.",
    )

    console.print(
        "The API URL is the address used by this machine "
        "to communicate with NexoraControl.\n"
    )

    console.print("[dim]Example: https://nexora.example.com/api/v1/[/dim]\n")

    api_url = Prompt.ask(
        "[bold]NexoraControl API URL[/bold]",
        default=settings.api_url,
    ).strip()

    if not api_url:
        show_error(
            "API URL cannot be empty",
            "Please provide the address of your NexoraControl API.",
        )
        return None

    if not is_valid_api_url(api_url):
        show_error(
            "Invalid API URL",
            "The URL must start with http:// or https:// " "and contain a valid host.",
        )
        return None

    # ============================================================
    # STEP 2 — MACHINE
    # ============================================================

    clear_and_render()

    render_step(
        2,
        3,
        "Machine identification",
        "Choose how this machine will appear in NexoraControl.",
    )

    hostname = get_system_hostname()
    ip = get_public_ip_native()
    os = get_os_info()

    console.print(f"Detected hostname: [cyan]{hostname}[/cyan]\n")

    console.print(
        "[dim]This name will be displayed in the NexoraControl dashboard.[/dim]\n"
    )

    name = Prompt.ask(
        "[bold]Machine name[/bold]",
        default=hostname,
    ).strip()

    if not name:
        show_error(
            "Machine name cannot be empty",
            "Please provide a name for this machine.",
        )
        return None

    # ============================================================
    # STEP 3 — REGISTRATION
    # ============================================================

    clear_and_render()

    render_step(
        3,
        3,
        "Registration",
        "NexoraControl will now register this machine and issue "
        "its authentication credentials.",
    )

    console.print(
        f"Machine: [cyan]{name}[/cyan]\n"
        f"Hostname: [cyan]{hostname}[/cyan]\n"
        f"API: [cyan]{api_url}[/cyan]\n"
    )

    console.print()

    payload = {"name": name, "hostname": hostname, "ip": ip, "os": os}
    client = BasicClient(base_url=api_url)

    response, status = await request_with_live_spinner(client, "create_agent", payload)

    if not response:
        return

    agent_id = response.get("id")
    token = response.get("token")

    if not agent_id or not token:
        show_error(
            "Invalid API response",
            "The server did not return the required agent ID "
            "or authentication token.",
        )
        return None

    # ============================================================
    # SAVE CONFIGURATION
    # ============================================================

    try:
        with Status(
            "[cyan]Saving agent configuration...[/cyan]",
            console=console,
        ):
            save_config(
                api_url=api_url,
                agent_id=agent_id,
                token=token,
                heartbeat_interval=config("NEXORA_HEARTBEAT_INTERVAL", cast=int),
                command_interval=config("NEXORA_COMMAND_INTERVAL", cast=int),
            )

    except OSError as exc:
        show_error(
            "Configuration save failed",
            str(exc),
        )
        return None

    settings = Settings(
        api_url=api_url,
        agent_id=agent_id,
        token=token,
        heartbeat_interval=settings.heartbeat_interval,
        command_interval=settings.command_interval,
    )

    # init new BasicClient with updated config
    client = BasicClient(settings)

    # collect the agent system information
    system_agent_info = ProductionParser.collect()

    # send a request with the system information after save the config
    response = await request_with_live_spinner(
        client, "send_system_info", system_agent_info
    )

    clear_and_render()

    show_success(
        "Agent registered successfully",
        "The machine has been connected to NexoraControl.",
    )

    show_configuration(
        api_url=settings.api_url,
        agent_id=settings.agent_id,
        hostname=hostname,
        name=name,
    )

    console.print()
    console.print(
        "[green]✓[/green] Authentication credentials saved\n"
        "[green]✓[/green] Configuration saved\n"
        "[green]✓[/green] Agent is ready to start\n"
    )

    return settings
