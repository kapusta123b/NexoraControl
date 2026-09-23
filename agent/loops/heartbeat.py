import asyncio

from api.client import BasicClient

from services.metrics.disk import _collect_storage_data
from services.metrics.cpu import _collect_cpu_metrics
from services.metrics.memory import _collect_memory_metrics


def collect_metrics() -> dict:
    return {
        "cpu_metrics": {**_collect_cpu_metrics()},
        "memory_metrics": {**_collect_memory_metrics()},
        "storage_metrics": {**_collect_storage_data()},
    }


async def heartbeat_loop(client: BasicClient) -> None:
    while True:
        data = collect_metrics()

        await client.send_heartbeat(heartbeat=data)

        await asyncio.sleep(client.settings.heartbeat_interval)


