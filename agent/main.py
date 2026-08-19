import asyncio
import os
import sys

from rich.console import Console

from api.client import BasicClient
from bootstrap.setup import setup_agent
from config.config import load_settings
from loops.commands import get_command_loop
from loops.heartbeat import heartbeat_loop

console = Console()


async def run():
    settings = load_settings()

    if not settings.agent_id or not settings.token:
        console.print(
            "[bold red]Agent is not configured.[/bold red]"
        )
        return

    client = BasicClient(settings)

    await asyncio.gather(
        heartbeat_loop(client),
        get_command_loop(client),
    )


async def setup():
    await setup_agent()


async def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "run"

    if mode == "setup":
        await setup()
        os._exit(0)

    if mode == "run":
        await run()
        return

    console.print(
        "[bold red]Unknown command.[/bold red]"
    )


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print(
            "\n[bold yellow]Agent stopped by user.[/bold yellow]"
        )