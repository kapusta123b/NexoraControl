import asyncio

from services.loop.system_info import _get_system_info
from config.config import HEARTBEAT_INTERVAL
from api.client import BasicClient


async def heartbeat_loop():
    client = BasicClient()

    while True:
        data = _get_system_info()

        await client.send_heartbeat(heartbeat=data)

        await asyncio.sleep(HEARTBEAT_INTERVAL)
