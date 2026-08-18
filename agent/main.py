import asyncio
import time

from rich.console import Console

from rich.spinner import Spinner
from rich.live import Live

from api.client import BasicClient
from bootstrap.setup import setup_agent
from loops.commands import get_command_loop
from loops.heartbeat import heartbeat_loop

console = Console()

async def main():
    settings = await setup_agent()

    if settings is None:
        return

    client = BasicClient(settings)

    await asyncio.gather(
        heartbeat_loop(client),
        get_command_loop(client),
    )


async def run_agent():
    with Live(
        Spinner(
            "dots",
            text="[bold green]Agent is running... [dim](Ctrl+C to exit)[/dim]",
        ),
        refresh_per_second=10,
        console=console,
    ):
        await main()


if __name__ == "__main__":
    try:
        asyncio.run(run_agent())

    except KeyboardInterrupt:
        console.print(
            "\n[bold red]✖[/bold red] "
            "[yellow]Agent stopped by user.[/yellow]"
        )