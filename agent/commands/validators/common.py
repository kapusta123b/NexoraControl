import re

from commands.catalog import COMMANDS_BY_ID


def validate_payload(payload: dict, fields: dict) -> dict[str, str]:
    if not isinstance(payload, dict):
        return {"payload": "Payload must be a JSON object."}

    errors: dict[str, str] = {}
    for unknown in payload.keys() - fields.keys():
        errors[unknown] = "Unknown parameter for this command."

    for key, spec in fields.items():
        present = key in payload and payload[key] is not None
        value = payload.get(key)
        required = spec.get("required", False)
        kind = spec["type"]

        if not present or (kind == "string" and value == ""):
            if required:
                errors[key] = "This field is required."
            continue

        if kind == "boolean":
            if type(value) is not bool:
                errors[key] = "Expected a boolean."
            elif spec.get("must_be_true") and value is not True:
                errors[key] = "You must explicitly acknowledge this action."

        elif kind == "integer":
            if type(value) is not int:
                errors[key] = "Expected an integer."
            elif value < spec.get("min", -(2**63)) or value > spec.get(
                "max", 2**63 - 1
            ):
                errors[key] = (
                    f"Must be between {spec.get('min')} and {spec.get('max')}."
                )

        elif kind == "float":
            if type(value) not in (int, float):
                errors[key] = "Expected a number."
            elif value < spec.get("min", float("-inf")) or value > spec.get(
                "max", float("inf")
            ):
                errors[key] = "Number is outside the allowed range."

        elif kind == "choice":
            if not isinstance(value, str) or value not in spec["choices"]:
                errors[key] = "Value must be one of the available choices."

        elif kind == "string":
            if not isinstance(value, str):
                errors[key] = "Expected a string."
            elif (
                "\x00" in value
                or any(ord(ch) < 32 for ch in value)
                or len(value) > spec.get("max_length", 512)
            ):
                errors[key] = "Invalid characters or string is too long."

            elif "must_equal" in spec and value != spec["must_equal"]:
                errors[key] = f"Type {spec['must_equal']} exactly to confirm."

            elif "pattern" in spec and not re.fullmatch(spec["pattern"], value):
                errors[key] = "Value does not match the required format."
            elif key in ("path", "compose_file") and (
                "/../" in value or value.endswith("/..")
            ):
                errors[key] = "Parent-directory traversal is not allowed."

        else:
            errors[key] = f"Unknown schema type: {kind}."

    return errors


def validator_for(command_id: str):
    fields = COMMANDS_BY_ID[command_id]["fields"]

    def validator(payload: dict) -> dict[str, str]:
        return validate_payload(payload, fields)

    validator.__name__ = f"validate_{command_id}"

    return validator
