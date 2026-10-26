from apps.agents.api.authentication import AgentTokenAuthentication

from rest_framework.permissions import IsAuthenticated

from rest_framework import generics, status

from rest_framework.mixins import CreateModelMixin
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.agents.api.pagination import AgentPagination


from django_filters.rest_framework import DjangoFilterBackend

from apps.agents.api.serializers.detail import (
    AgentDetailSerializer,
    AgentHeartbeatSerializer,
    AgentSystemInfoSerializer,
)
from apps.agents.api.serializers.create import AgentListCreateSerializer

from apps.agents.models.agent import Agent
from apps.agents.models.agent_information import AgentSystemInfo

from apps.agents.selectors.agents import register_new_agent

from apps.agents.services.heartbeat import heartbeat_manager


class AgentListView(generics.ListCreateAPIView):
    queryset = Agent.objects.all().order_by("-pk")
    serializer_class = AgentListCreateSerializer

    pagination_class = AgentPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = ["status", "hostname"]
    search_fields = ["hostname"]
    ordering_fields = ["status", "hostname", "id"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        agent_id, token = register_new_agent(serializer.validated_data)

        return Response(
            {"id": agent_id, "token": token},
            status=status.HTTP_201_CREATED,
            headers={"Cache-Control": "no-store"},
        )


class AgentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()

    serializer_class = AgentDetailSerializer


class AgentHeartbeatView(APIView):
    authentication_classes = [AgentTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        agent = request.user

        serializer = AgentHeartbeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        metrics_data = dict(serializer.validated_data)
        metrics_data["uptime"] = request.data.get("uptime", 0)

        heartbeat_manager(metrics_data, agent)

        return Response(status=status.HTTP_200_OK)


class AgentSystemInformation(
    CreateModelMixin,
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = AgentSystemInfo.objects.all()
    serializer_class = AgentSystemInfoSerializer

    lookup_field = "agent_id"
    lookup_url_kwarg = "pk"

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(agent_id=self.kwargs["pk"])
