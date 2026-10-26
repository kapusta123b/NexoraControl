from .common import validator_for

system_processes_validator = validator_for("system_processes")

_FORBIDDEN_NON_SERVICE_SUFFIXES = (
    ".target",
    ".socket",
    ".slice",
    ".timer",
    ".mount",
    ".path",
    ".automount",
)


def service_validator_for(command_id: str):
    base = validator_for(command_id)

    def validator(payload: dict) -> dict:
        errors = base(payload)
        if errors or not isinstance(payload, dict):
            return errors
        name = payload.get("service", "")
        if name.endswith(_FORBIDDEN_NON_SERVICE_SUFFIXES):
            errors["service"] = "Only service units may be managed."
        return errors

    validator.__name__ = f"validate_service_{command_id}"
    return validator
