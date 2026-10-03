from apps.agents.api.authentication import AgentTokenAuthentication

from rest_framework.permissions import IsAuthenticated

from rest_framework import status

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
)

from rest_framework.response import Response

from rest_framework.views import APIView


from apps.agents.api.serializers.detail import (
    AgentDetailSerializer,
    AgentHeartbeatSerializer,
)
from apps.agents.api.serializers.create import AgentListCreateSerializer
from apps.agents.models.agent import Agent
from apps.agents.selectors.agents import register_new_agent

from apps.agents.services.heartbeat import heartbeat_manager


class AgentListView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AgentListCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        agent_id, token = register_new_agent(serializer.validated_data)

        return Response(
            {"id": agent_id, "token": token}, status=status.HTTP_201_CREATED
        )


class AgentDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()

    serializer_class = AgentDetailSerializer


class AgentHeartbeatView(APIView):
    authentication_classes = [AgentTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        agent = request.user

        serializer = AgentHeartbeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        metrics_data = serializer.validated_data

        heartbeat_manager(metrics_data, agent)

        return Response(status=status.HTTP_200_OK)
