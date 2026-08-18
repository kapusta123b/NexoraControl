import asyncio

from services.loop.system_info import _get_system_info


async def heartbeat_loop(client):

    while True:
        data = _get_system_info()

        await client.send_heartbeat(heartbeat=data)

        await asyncio.sleep(client.settings.heartbeat_interval)
