from commands.docker.registry import COMMAND_DOCKER
from api.client import BasicClient
from .system.registry import COMMAND_SYSTEM

from datetime import datetime, timezone

COMMANDS = COMMAND_SYSTEM | COMMAND_DOCKER


async def command_parser(commands: list) -> None:
    finished_commands = []

    for command_data in commands:
        command_type = command_data["command_type"]
        payload = command_data["payload"]

        result = {"id": command_data["id"], "errors": {}}

        command = COMMANDS.get(command_type)

        if command is None:
            result.update(
                {
                    "status": "FAILED",
                    "output": "Command not found",
                }
            )

            result["finished_at"] = datetime.now(timezone.utc).isoformat()
            finished_commands.append(result)

            continue

        if isinstance(command, tuple):
            func, validator = command

            errors = validator(payload)

            if errors:
                result.update(
                    {
                        "status": "FAILED",
                        "errors": errors,
                    }
                )
            else:
                result.update(func(payload))

        else:
            result.update(command(payload))

        result["finished_at"] = datetime.now(timezone.utc).isoformat()

        finished_commands.append(result)

    if finished_commands:
        await BasicClient().send_commands(finished_commands)
