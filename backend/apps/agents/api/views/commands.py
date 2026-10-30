from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from apps.agents.models.command import Command
from apps.agents.api.serializers.command import (
    CommandListSerializer,
    CommandPatchSerializer,
    CommandPendingListSerializer,
)

from apps.agents.api.pagination import AgentPagination

from apps.agents.selectors.commands import (
    get_command_queryset,
)

from rest_framework.exceptions import ValidationError

from apps.agents.services.command import (
    bulk_update_agent_commands,
    update_commands_status,
)


class CommandListView(ListCreateAPIView):
    serializer_class = CommandListSerializer

    pagination_class = AgentPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]

    filterset_fields = {
        "status": ["exact"],
        "command_type": ["exact", "in"],
    }

    search_fields = ["command_type", "status"]
    ordering_fields = ["status", "created_at", "started_at", "finished_at"]

    def perform_create(self, serializer):
        serializer.save(agent_id=self.kwargs["pk"])

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        queryset = get_command_queryset(self.request, pk)

        return queryset


class CommandPendingListView(ListCreateAPIView):
    serializer_class = CommandPendingListSerializer

    def get_queryset(self):
        return Command.objects.filter(
            agent_id=self.kwargs["pk"],
            status=Command.Status.PENDING,
        )

    def list(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())

        update_commands_status(queryset)

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)


class CommandBulkUpdateView(APIView):
    def patch(self, request, pk):
        if not isinstance(request.data, list):
            raise ValidationError({"detail": "Must be a list (JSON array)."})

        serializer = CommandPatchSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        has_updated = bulk_update_agent_commands(serializer.validated_data, agent_id=pk)

        if has_updated:
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_204_NO_CONTENT)
