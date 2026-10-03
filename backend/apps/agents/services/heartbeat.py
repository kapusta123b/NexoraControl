from django.db import transaction

from django.utils import timezone

from apps.agents.models.agent import Agent
from apps.agents.models.metric import AgentMetric

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def _normalize_storage_data(metrics_data: dict):
    storage_devices = {}
    file_systems = {}

    for device_name, device_info in metrics_data["storage_metrics"].items():
        if "mount" in device_info:
            file_systems[device_name] = device_info
        else:
            storage_devices[device_name] = {
                "model": device_info["model"],
                "type": device_info["type"],
                "capacity": device_info["capacity"],
                "status": device_info["status"],
                "write_bytes": device_info["write_bytes"],
                "read_bytes": device_info["read_bytes"],
                "write_count": device_info["write_count"],
                "read_count": device_info["read_count"],
            }

    metrics_data["storage_metrics"] = {
        device_name: {
            "write_bytes": device_info["write_bytes"],
            "read_bytes": device_info["read_bytes"],
        }
        for device_name, device_info in metrics_data["storage_metrics"].items()
        if "mount" not in device_info
    }

    return metrics_data, {**storage_devices, **file_systems}


def _normalize_thermal_data(metrics_data: dict):
    thermal_metrics = {}

    for hardware, sensors in metrics_data["thermal_metrics"].items():
        device_index = 0
        current_device_name = hardware
        seen_labels_in_sub = set()

        for sensor in sensors:
            label = sensor["label"]
            current_temp = sensor["current"]

            if label in seen_labels_in_sub:
                device_index += 1
                current_device_name = f"{hardware}_{device_index}"
                seen_labels_in_sub = set()

            if device_index == 0 and any(
                s["label"] == label for s in sensors if s is not sensor
            ):
                current_device_name = f"{hardware}_0"

            if current_device_name not in thermal_metrics:
                thermal_metrics[current_device_name] = {}

            thermal_metrics[current_device_name][label] = current_temp
            seen_labels_in_sub.add(label)

    raw_thermal_metrics = metrics_data["thermal_metrics"]
    metrics_data["thermal_metrics"] = thermal_metrics

    return metrics_data, raw_thermal_metrics


def _normalize_heartbeat_data(metrics_data: dict):
    metrics_data, storage_data = _normalize_storage_data(metrics_data)
    metrics_data, thermal_data = _normalize_thermal_data(metrics_data)

    channel_layer_data = {**storage_data, **thermal_data}

    channel_layer_data = {
        **storage_data,
        **thermal_data,
        "cpu_metrics": metrics_data["cpu_metrics"],
        "memory_metrics": metrics_data["memory_metrics"],
    }

    return metrics_data, channel_layer_data


def heartbeat_manager(metrics_data: dict, agent):

    metrics_data, channel_layer_data = _normalize_heartbeat_data(metrics_data)

    now = timezone.now()

    with transaction.atomic():
        AgentMetric.objects.create(
            agent=agent,
            **metrics_data,
        )
        agent.status = Agent.Status.ONLINE
        agent.last_seen = now
        agent.save(update_fields=["status", "last_seen"])

    channel_layer = get_channel_layer()

    if channel_layer:
        channel_layer_data["timestamp"] = int(now.timestamp())

        async_to_sync(channel_layer.group_send)(
            f"agent_{agent.id}",
            {
                "type": "send_agent_metrics",
                "metrics": channel_layer_data,
            },
        )
