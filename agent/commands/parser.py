from commands.docker.registry import COMMAND_DOCKER
from api.client import BasicClient
from .system.registry import COMMAND_SYSTEM

from datetime import datetime, timezone

COMMANDS = COMMAND_SYSTEM | COMMAND_DOCKER

async def command_parser(json: list) -> None:
    finished_commands = []

    if json:
        for command in json:
            command_type = command["command_type"]
            payload = command["payload"]

            func = COMMANDS.get(command_type, None)

            if func is None:
                break

            data = func(payload)

            data["id"] = command["id"]
            data["finished_at"] = datetime.now(timezone.utc).isoformat()

            finished_commands.append(data)

    await BasicClient().send_commands(finished_commands)