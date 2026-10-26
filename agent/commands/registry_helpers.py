from commands.catalog import COMMANDS_BY_ID
from commands.validators.common import validator_for


def register_handlers(
    module, names: list[str], output_parsers: dict | None = None
) -> dict:
    output_parsers = output_parsers or {}
    registry = {}

    for name in names:
        spec = COMMANDS_BY_ID[name]
        registry[name] = {
            "handler": getattr(module, name),
            "validator": validator_for(name),
            "timeout": spec.get("timeout", 12),
        }

        if name in output_parsers:
            registry[name]["output_parser"] = output_parsers[name]

    return registry
