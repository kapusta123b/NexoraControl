from api.client import BasicClient
from .system.registry import COMMAND_SYSTEM

COMMANDS = COMMAND_SYSTEM

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

            finished_commands.append(data)

    await BasicClient().send_commands(finished_commands)