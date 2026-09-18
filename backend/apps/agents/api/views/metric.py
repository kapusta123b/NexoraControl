from datetime import timedelta
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.agents.models.metric import AgentMetric


from datetime import timedelta
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.agents.models import Agent, AgentMetric


class AgentMetricHistoryView(APIView):
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
                "cpu_load",
                "ram_load",
                "load_average",
                "cpu_load_per_core",
            )
        )

        timestamps = []
        cpu_values = []
        ram_values = []
        load_average = []
        cpu_load_per_core = []
        cpu_load_per_core_timestamps = []

        for created_at, cpu, ram, load, cores in raw_metrics:
            ts = int(created_at.timestamp())
            timestamps.append(ts)
            cpu_values.append(cpu)
            ram_values.append(ram)
            load_average.append(load)

            if ts >= one_minute_ago_ts:
                cpu_load_per_core.append(cores)
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


class AgentMetricLatestView(APIView):
    def get(self, request, pk):
        hours = int(request.GET.get("hours", 1))
        start_time = timezone.now() - timedelta(hours=hours)
        latest = (
            AgentMetric.objects.filter(agent_id=pk, created_at__gte=start_time)
            .order_by("-created_at")
            .first()
        )

        if not latest:
            return Response({})

        return Response(
            {
                "timestamp": int(latest.created_at.timestamp()),
                "cpu_value": latest.cpu_load,
                "ram_value": latest.ram_load,
                "ram_used": latest.ram_used_bytes,
                "ram_available": latest.ram_available_bytes,
                "load_average": latest.load_average,
                "cpu_per_core": latest.cpu_load_per_core,
            }
        )
