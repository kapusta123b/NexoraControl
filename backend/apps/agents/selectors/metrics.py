import datetime

from datetime import timedelta

from typing import Any

from django.utils import timezone

from django.shortcuts import get_object_or_404

from rest_framework.exceptions import ValidationError

from apps.agents.models import Agent, AgentMetric


def _get_metric_fields_by_time(
    request: Any, pk: int, now: datetime.datetime, fields: tuple[str, ...]
) -> dict[str, dict] | None:
    try:
        hours = int(request.GET.get("hours", 1))
        if hours <= 0:
            raise ValueError

    except ValueError:
        raise ValidationError(
            {"hours": "Invalid 'hours' parameter. Must be a positive integer."}
        )

    start_time = now - timedelta(hours=hours)

    if not isinstance(fields, tuple) or not all(
        isinstance(field, str) for field in fields
    ):
        raise TypeError("fields argument must be a tuple of strings")

    return (
        AgentMetric.objects.filter(agent_id=pk, created_at__gte=start_time)
        .order_by("created_at")
        .values_list(*fields)
    )


def get_resource_metrics(request: Any, pk: int) -> dict[str, list] | None:
    get_object_or_404(Agent, pk=pk)

    now = timezone.now()
    raw_metrics = _get_metric_fields_by_time(
        request, pk, now, fields=("created_at", "cpu_metrics", "memory_metrics")
    )

    one_minute_ago_ts = (now - timedelta(minutes=1)).timestamp()

    timestamps = []
    cpu_values = []
    ram_values = []
    load_average = []
    cpu_load_per_core = []
    cpu_load_per_core_timestamps = []

    for created_at, cpu_metrics, memory_metrics in raw_metrics:
        ts = int(created_at.timestamp())
        timestamps.append(ts)
        cpu_values.append(cpu_metrics.get("cpu_load", 0.0))
        ram_values.append(memory_metrics.get("ram_load", 0.0))
        load_average.append(cpu_metrics.get("load_average", [0.0, 0.0, 0.0]))

        if ts >= one_minute_ago_ts:
            cpu_load_per_core.append(cpu_metrics.get("cpu_load_per_core", []))
            cpu_load_per_core_timestamps.append(ts)

    return {
        "timestamps": timestamps,
        "cpu_values": cpu_values,
        "ram_values": ram_values,
        "load_average": load_average,
        "cpu_load_per_core": cpu_load_per_core,
        "cpu_load_per_core_timestamps": cpu_load_per_core_timestamps,
    }


def get_storage_metrics(request: Any, pk: int) -> dict[str, dict | list] | None:
    get_object_or_404(Agent, pk=pk)

    target_disk = request.GET.get("disk", None)

    only_disks_names = request.GET.get("disks_names", "false").lower() == "true"

    if only_disks_names:

        return {
            "disks_names": list(
                AgentMetric.objects.filter(agent_id=pk)
                .order_by("-created_at")
                .first()
                .storage_metrics.keys()
            ),
        }

    now = timezone.now()

    raw_metrics = _get_metric_fields_by_time(
        request, pk, now, fields=("created_at", "storage_metrics")
    )
    timestamps = []

    disks_read_write_data = {}

    for created_at, storage_metrics in raw_metrics:
        timestamps.append(int(created_at.timestamp()))

        if target_disk:
            if target_disk in storage_metrics:
                disk_info = storage_metrics[target_disk]

                if target_disk not in disks_read_write_data:
                    disks_read_write_data[target_disk] = {"write": [], "read": []}

                disks_read_write_data[target_disk]["write"].append(
                    disk_info["write_bytes"]
                )
                disks_read_write_data[target_disk]["read"].append(
                    disk_info["read_bytes"]
                )

        else:
            for disk_name, disk_info in storage_metrics.items():
                write_bytes = disk_info["write_bytes"]
                read_bytes = disk_info["read_bytes"]

                if disk_name not in disks_read_write_data:
                    disks_read_write_data[disk_name] = {
                        "write": [write_bytes],
                        "read": [read_bytes],
                    }

                else:
                    disks_read_write_data[disk_name]["write"].append(write_bytes)
                    disks_read_write_data[disk_name]["read"].append(read_bytes)

    return {"timestamps": timestamps, "storage_metrics": disks_read_write_data}


def get_thermal_metrics(request: Any, pk: int) -> dict[str] | None:
    get_object_or_404(Agent, pk=pk)

    target_hardware = request.GET.get("hardware", None)

    only_hardware_names = request.GET.get("hardware_names", "false").lower() == "true"

    requested_sensors = request.GET.get("sensors", None)

    if isinstance(requested_sensors, str):
        requested_sensors = [s.lower().strip() for s in requested_sensors.split(",")]

    if only_hardware_names:
        hardware_with_sensors = {}
        last_metric = (
            AgentMetric.objects.filter(agent_id=pk).order_by("-created_at").first()
        )
        for hardware, sensors in last_metric.thermal_metrics.items():
            hardware_with_sensors[hardware] = list(sensors.keys())

        return {"hardwares_names": hardware_with_sensors}

    now = timezone.now()

    raw_metrics = _get_metric_fields_by_time(
        request, pk, now, fields=("created_at", "thermal_metrics")
    )

    timestamps = []
    thermal_data = {}

    has_sensor_filter = bool(requested_sensors)

    for created_at, thermal_metrics in raw_metrics:
        if not thermal_metrics:
            continue

        if target_hardware and target_hardware not in thermal_metrics:
            continue

        timestamps.append(int(created_at.timestamp()))

        for hardware, sensors in thermal_metrics.items():
            if target_hardware and hardware != target_hardware:
                continue

            if hardware not in thermal_data:
                thermal_data[hardware] = {}

            for sensor, value in sensors.items():
                if has_sensor_filter:
                    sensor_lower = sensor.lower().strip()

                    if sensor_lower not in requested_sensors:
                        continue

                if sensor not in thermal_data[hardware]:
                    thermal_data[hardware][sensor] = []

                thermal_data[hardware][sensor].append(value)

    if target_hardware and target_hardware not in thermal_data:
        raise ValidationError(
            {
                "hardware": f"Hardware with that name does not exist or has no metrics: '{target_hardware}'"
            }
        )

    return {"timestamps": timestamps, "thermal_metrics": thermal_data}


def get_network_metrics(request: Any, pk: int) -> dict[str, dict | list] | None:
    get_object_or_404(Agent, pk=pk)

    target_network = request.GET.get("network", None)
    only_network_names = request.GET.get("network_names", "false").lower() == "true"
    fields = request.GET.get("fields", None)

    if isinstance(fields, str):
        requested_fields = [s.lower().strip() for s in fields.split(",")]

    if only_network_names:
        last_metric = (
            AgentMetric.objects.filter(agent_id=pk).order_by("-created_at").first()
        )
        network_names = list(last_metric.network_metrics.keys())

        return {"network_names": network_names}

    now = timezone.now()

    raw_metrics = _get_metric_fields_by_time(
        request, pk, now, fields=("created_at", "network_metrics")
    )

    timestamps = []
    network_data = {}

    for created_at, network_metrics in raw_metrics:
        if not network_metrics:
            continue

        if target_network and target_network not in network_metrics:
            continue

        timestamps.append(int(created_at.timestamp()))

        for network_name, network_info in network_metrics.items():
            if target_network and network_name != target_network:
                continue

            if network_name not in network_data:
                network_data[network_name] = {}

            for key, value in network_info.items():
                if requested_fields:
                    key_lower = key.lower().strip()

                    if key_lower not in requested_fields:
                        continue

                if "traffic" in key:
                    type_of_data = "traffic"

                if "packets" in key:
                    type_of_data = "packets"

                if type_of_data not in network_data[network_name]:
                    network_data[network_name][type_of_data] = {}

                if key not in network_data[network_name][type_of_data]:
                    network_data[network_name][type_of_data][key] = []

                network_data[network_name][type_of_data][key].append(value)

    if target_network and target_network not in network_data:
        raise ValidationError(
            {
                "network": f"Network name with that name does not exist or has no metrics: '{target_network}'"
            }
        )

    return {"timestamps": timestamps, "network_metrics": network_data}
