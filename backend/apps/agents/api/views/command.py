from rest_framework import status
from rest_framework.generics import ListCreateAPIView, UpdateAPIView

from rest_framework.response import Response

from rest_framework.views import APIView

from apps.agents.models.command import Command
from apps.agents.api.serializers.command import (
    CommandListSerializer,
    CommandPatchSerializer,
)

from apps.agents.models.agent import Agent


class CommandListView(ListCreateAPIView):
    serializer_class = CommandListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pk = self.kwargs["pk"]
        agent = objects.get(id=pk)

        command = serializer.save(agent=agent)

        return Response(
            {"status": "ok"},
            status=status.HTTP_201_CREATED,
        )

    def get_queryset(self):
        pk = self.kwargs["pk"]
        return (
            Command.objects.filter(agent_id=pk)
            .select_related("agent")
            .order_by("-created_at")
        )


class CommandBulkCreateView(APIView):

    def patch(self, request, *args, **kwargs):

        if not isinstance(request.data, list):
            return Response(
                {"detail": "must be a list {JSON array}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = CommandPatchSerializer(data=request.data, many=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        command_ids = [item["id"] for item in validated_data]

        commands_dict = {c.id: c for c in Command.objects.filter(id__in=command_ids)}

        commands_to_update = []

        for item in validated_data:
            command_id = item["id"]

            if command_id in commands_dict:

                command = commands_dict[command_id]
                command.status = item["status"]
                commands_to_update.append(command)

        if commands_to_update:
            Command.objects.bulk_update(commands_to_update, ["status"])

        return Response({"status": "ok"}, status=status.HTTP_201_CREATED)
