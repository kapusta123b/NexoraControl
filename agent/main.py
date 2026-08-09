import asyncio

from loops.commands import get_command_loop
from loops.heartbeat import heartbeat_loop


async def main():

    await asyncio.gather(
        heartbeat_loop(),
        get_command_loop(),
    )


if __name__ == "__main__":
    asyncio.run(main())