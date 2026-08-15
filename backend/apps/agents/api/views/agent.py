from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView
from rest_framework.response import Response


from apps.agents.models.agent import Agent
from apps.agents.api.serializers.create import AgentListCreateSerializer
from apps.agents.api.serializers.detail import (
    AgentDetailSerializer,
    AgentHeartbeatSerializer,
)

from django.utils import timezone


class AgentListView(ListCreateAPIView):
    queryset = Agent.objects.all().order_by('-status')
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

        token = request.headers.get("Authorization")

        agent = Agent.objects.filter(id=pk, token=token).first()
        if not agent:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )

        serializer = AgentHeartbeatSerializer(agent, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save(status=Agent.Status.ONLINE, last_seen=timezone.now())

        return Response({"status": "ok"}, status=status.HTTP_200_OK)