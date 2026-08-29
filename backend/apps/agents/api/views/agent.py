from datetime import datetime, timezone as datetime_timezone

from django.db import transaction
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.agents.api.serializers.detail import (
    AgentDetailSerializer,
    AgentHeartbeatSerializer,
)
from apps.agents.api.serializers.create import AgentListCreateSerializer
from apps.agents.models.agent import Agent
from apps.agents.models.metric import AgentMetric


class AgentListView(ListCreateAPIView):
    queryset = Agent.objects.all().order_by("-status")
    serializer_class = AgentListCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        agent = serializer.save()

        return Response(
            {
                "id": agent.id,
                "token": str(agent.token),
            },
            status=status.HTTP_201_CREATED,
        )


class AgentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()

    serializer_class = AgentDetailSerializer


class AgentHeartbeatView(APIView):

    def post(self, request, pk):
        auth_header = request.headers.get("Authorization", "")
        token = auth_header.split(" ")[1] if " " in auth_header else auth_header

        agent = Agent.objects.filter(id=pk, token=token).first()
        if not agent:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = AgentHeartbeatSerializer(agent, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            AgentMetric.objects.create(
                agent=agent,
                cpu_load=serializer.validated_data.get("cpu_load"),
                ram_load=serializer.validated_data.get("ram_load"),
            )
            serializer.save(status=Agent.Status.ONLINE, last_seen=timezone.now())

        return Response({"status": "ok"}, status=status.HTTP_200_OK)

    def get(self, request: Request, pk):
        from_ts_str = request.GET.get("from_date")

        if not from_ts_str:
            return Response({"error": "Missing from_date timestamp"}, status=400)

        try:
            from_timestamp = int(from_ts_str)

        except ValueError:
            return Response({"error": "from_date must be a unix timestamp"}, status=400)

        start_time = datetime.fromtimestamp(from_timestamp, tz=datetime_timezone.utc)

        metrics = (
            AgentMetric.objects
            .filter(agent_id=pk, created_at__gte=start_time)
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
