import asyncio

from api.client import BasicClient

from services.metrics.thermals import collect_thermal_metrics
from services.metrics.disk import collect_storage_data
from services.metrics.cpu import collect_cpu_metrics
from services.metrics.memory import collect_memory_metrics


def collect_metrics() -> dict:
    return {
        "cpu_metrics": {**collect_cpu_metrics()},
        "memory_metrics": {**collect_memory_metrics()},
        "storage_metrics": {**collect_storage_data()},
        "thermal_metrics": {**collect_thermal_metrics()},
    }


async def heartbeat_loop(client: BasicClient) -> None:
    while True:
        data = collect_metrics()

        await client.send_heartbeat(heartbeat=data)

        await asyncio.sleep(client.settings.heartbeat_interval)
