import psutil
import asyncio

from config.config import HEARTBEAT_INTERVAL
from api.client import BasicClient

def _get_system_info() -> dict:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    return {"cpu_load": round(cpu), "ram_load": round(ram)}


async def heartbeat_loop():
    client = BasicClient()

    while True:
        data = _get_system_info()

        await client.send_heartbeat(params=data)

        await asyncio.sleep(HEARTBEAT_INTERVAL)
