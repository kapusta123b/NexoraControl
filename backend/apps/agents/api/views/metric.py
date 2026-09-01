from datetime import timedelta

from rest_framework.views import APIView

from rest_framework.response import Response

from apps.agents.models.metric import AgentMetric

from django.utils import timezone


class ResourceMetric(APIView):

    def get(self, request, pk):
        hours_str = request.GET.get("hours")

        if not hours_str:
            return Response({"error": "Missing from_date timestamp"}, status=400)

        try:
            hours = int(hours_str)

        except ValueError:
            return Response({"error": "from_date must be a unix timestamp"}, status=400)

        start_time = timezone.now() - timedelta(hours=hours)

        metrics = (
            AgentMetric.objects.filter(agent_id=pk, created_at__gte=start_time)
            .order_by("created_at")
            .values("created_at", "cpu_load", "ram_load")
        )

        timestamps = []
        cpu_values = []
        ram_values = []

        for m in metrics:
            timestamps.append(int(m["created_at"].timestamp()))
            cpu_values.append(m["cpu_load"])
            ram_values.append(m["ram_load"])

        return Response(
            {
                "timestamps": timestamps,
                "cpu_values": cpu_values,
                "ram_values": ram_values,
            }
        )
