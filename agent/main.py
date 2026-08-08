import asyncio

from loops.heartbeat import heartbeat_loop


async def main():

    await asyncio.gather(
        heartbeat_loop(),
    )


if __name__ == "__main__":
    asyncio.run(main())