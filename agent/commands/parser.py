from commands.executor import subprocess_executor
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

        result = {
            "id": command_data["id"],
            "errors": {},
            "started_at": datetime.now(timezone.utc).isoformat(),
        }

        definition = COMMANDS.get(command_type)

        if definition is None:
            result.update(
                {
                    "status": "FAILED",
                    "output": "Command not found",
                }
            )

            result["finished_at"] = datetime.now(timezone.utc).isoformat()
            finished_commands.append(result)

            continue

        handler = definition["handler"]
        timeout = definition.get("timeout", 10)
        validator = definition.get("validator")
        output_parser = definition.get("output_parser")

        if validator:
            errors = validator(payload)

            if errors:
                result.update(
                    {
                        "status": "FAILED",
                        "errors": errors,
                    }
                )

                result["finished_at"] = datetime.now(timezone.utc).isoformat()
                finished_commands.append(result)

                continue

        command = handler(payload)

        executor_result = subprocess_executor(command, timeout)

        if output_parser and executor_result["status"] == "SUCCESS":
            parser_result = output_parser(executor_result, payload)
            result.update(parser_result)

        else:
            result.update(executor_result)

        result["finished_at"] = datetime.now(timezone.utc).isoformat()

        finished_commands.append(result)

    if finished_commands:
        await BasicClient().send_commands(finished_commands)
