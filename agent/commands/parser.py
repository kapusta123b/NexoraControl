"""Resolve registered command IDs, validate payloads and report every result.

Blocking command execution is offloaded from the asyncio loop, so agent heartbeats
are not held up by long-running Docker / journalctl operations.
"""

import asyncio
from datetime import datetime, timezone

from api.client import BasicClient
from commands.catalog import COMMANDS_BY_ID
from commands.docker.registry import COMMAND_DOCKER
from commands.executor import subprocess_executor, _limit
from commands.system.registry import COMMAND_SYSTEM

COMMANDS = COMMAND_SYSTEM | COMMAND_DOCKER


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


async def command_parser(commands: list[dict]) -> None:
    if not commands:
        return

    finished_commands = []

    for command_data in commands:
        result = {
            "id": command_data.get("id"),
            "errors": {},
            "started_at": _now(),
        }

        try:
            command_type = command_data.get("command_type")
            payload = command_data.get("payload")
            definition = COMMANDS.get(command_type)

            if not definition:
                result.update(status="FAILED", output="Command not registered on agent")
            else:
                errors = definition["validator"](payload)
                if errors:
                    result.update(
                        status="FAILED", errors=errors, output="Invalid command payload"
                    )
                else:
                    args = await asyncio.to_thread(definition["handler"], payload)

                    executed = await asyncio.to_thread(
                        subprocess_executor, args, definition.get("timeout", 12)
                    )

                    if executed["status"] == "SUCCESS" and definition.get(
                        "output_parser"
                    ):
                        executed = definition["output_parser"](executed, payload)
                    result.update(executed)
                    result["output"] = _limit(result.get("output", ""))

        except Exception as error:
            result.update(
                status="FAILED",
                errors={"execution": type(error).__name__},
                output=_limit(f"Command failed: {error}"),
            )

        result["finished_at"] = _now()
        finished_commands.append(result)

    await BasicClient().send_commands(finished_commands)
