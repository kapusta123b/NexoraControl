from django.db import transaction

from apps.agents.api.authentication import AgentTokenAuthentication

from rest_framework.permissions import IsAuthenticated

from rest_framework import status

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.response import Response

from rest_framework.views import APIView

from django.utils import timezone

from apps.agents.api.serializers.detail import (
    AgentDetailSerializer,
    AgentHeartbeatSerializer,
)
from apps.agents.api.serializers.create import AgentListCreateSerializer

from apps.agents.models.agent import Agent
from apps.agents.models.metric import AgentMetric


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


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
    authentication_classes = [AgentTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        agent = request.user

        if str(agent.id) != str(pk):
            return Response(
                {"error": "Token does not match agent ID"},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = AgentHeartbeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        metrics_data = serializer.validated_data

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
            socket_payload = dict(metrics_data)
            socket_payload["timestamp"] = int(now.timestamp())

            async_to_sync(channel_layer.group_send)(
                f"agent_{pk}",
                {
                    "type": "send_agent_metrics",
                    "metrics": socket_payload,
                },
            )

        return Response({"status": "ok"}, status=status.HTTP_200_OK)
