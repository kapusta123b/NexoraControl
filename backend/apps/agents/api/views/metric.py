from apps.agents.models.metric import AgentMetric

from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.agents.models import Agent, AgentMetric


class AgentResourceMetricHistoryView(APIView):
    def get(self, request, pk):
        try:
            hours = int(request.GET.get("hours", 1))
            if hours <= 0:
                raise ValueError
        except ValueError:
            return Response(
                {"detail": "Invalid 'hours' parameter. Must be a positive integer."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        get_object_or_404(Agent, pk=pk)

        now = timezone.now()
        start_time = now - timedelta(hours=hours)
        one_minute_ago_ts = (now - timedelta(minutes=1)).timestamp()

        raw_metrics = (
            AgentMetric.objects.filter(agent_id=pk, created_at__gte=start_time)
            .order_by("created_at")
            .values_list(
                "created_at",
                "cpu_metrics",
                "memory_metrics",
            )
        )

        timestamps = []
        cpu_values = []
        ram_values = []
        load_average = []
        cpu_load_per_core = []
        cpu_load_per_core_timestamps = []

        for created_at, cpu_metrics, memory_metrics in raw_metrics:
            ts = int(created_at.timestamp())
            timestamps.append(ts)
            cpu_values.append(cpu_metrics["cpu_load"])
            ram_values.append(memory_metrics["ram_load"])
            load_average.append(cpu_metrics["load_average"])

            if ts >= one_minute_ago_ts:
                cpu_load_per_core.append(cpu_metrics["cpu_load_per_core"])
                cpu_load_per_core_timestamps.append(ts)

        return Response(
            {
                "timestamps": timestamps,
                "cpu_values": cpu_values,
                "ram_values": ram_values,
                "load_average": load_average,
                "cpu_load_per_core": cpu_load_per_core,
                "cpu_load_per_core_timestamps": cpu_load_per_core_timestamps,
            }
        )


class AgentStorageMetricHistoryView(APIView):

    def get(self, request, pk):
        try:
            hours = int(request.GET.get("hours", 1))

            target_disk = request.GET.get("disk", None)

            only_disks_names = request.GET.get("disks_names", "false").lower() == "true"

            if hours <= 0:
                raise ValueError

        except ValueError:
            return Response(
                {"detail": "Invalid 'hours' parameter. Must be a positive integer."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        get_object_or_404(Agent, pk=pk)

        if only_disks_names:

            return Response(
                {
                    "disks_names": list(
                        AgentMetric.objects.filter(agent_id=pk)
                        .order_by("-created_at")
                        .first()
                        .storage_metrics.keys()
                    ),
                }
            )

        now = timezone.now()
        start_time = now - timedelta(hours=hours)

        raw_metrics = (
            AgentMetric.objects.filter(agent_id=pk, created_at__gte=start_time)
            .order_by("created_at")
            .values_list(
                "created_at",
                "storage_metrics",
            )
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

        return Response(
            {"timestamps": timestamps, "storage_metrics": disks_read_write_data}
        )
