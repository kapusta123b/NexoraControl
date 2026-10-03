from apps.agents.models.command import Command

from django.db import transaction


def update_commands_status(queryset):
    with transaction.atomic():
        Command.objects.select_for_update().filter(
            id__in=[command.id for command in queryset]
        ).update(status=Command.Status.RUNNING)


def bulk_update_agent_commands(validated_data: list[dict], agent_id: int) -> bool:
    command_ids = [item["id"] for item in validated_data]

    commands_dict = {
        c.id: c for c in Command.objects.filter(id__in=command_ids, agent_id=agent_id)
    }

    commands_to_update = []

    for item in validated_data:
        command_id = item["id"]

        if command_id in commands_dict:
            command = commands_dict[command_id]
            command.output = item.get("output", "")
            command.status = item["status"]
            command.errors = item.get("errors", {})
            command.started_at = item.get("started_at")
            command.finished_at = item.get("finished_at")

            commands_to_update.append(command)

    if commands_to_update:
        with transaction.atomic():
            Command.objects.bulk_update(
                commands_to_update,
                ["status", "output", "finished_at", "started_at", "errors"],
            )
        return True

    return False
