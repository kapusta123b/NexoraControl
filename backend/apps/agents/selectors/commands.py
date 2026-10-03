from rest_framework.exceptions import ValidationError

from apps.agents.models.command import Command


def get_command_queryset(request, pk):
    queryset = (
        Command.objects.filter(agent_id=pk)
        .select_related("agent")
        .order_by("-created_at")
    )

    status = request.query_params.get("status")
    if isinstance(status, str):
        queryset = queryset.filter(status=status.upper())
    else:
        raise ValidationError(
            {"status": "Invalid 'status' parameter. Must be a string."}
        )

    count = request.query_params.get("count")

    if count:
        try:
            count = int(count)

            queryset = queryset[:count]

        except ValueError:
            raise ValidationError(
                {"count": "Invalid 'status' parameter. Must be a positive integer."}
            )

    return queryset
