
def system_processes_validator(payload: dict) -> dict:
    errors = {}

    lines = payload.get("lines")

    if not lines:
        errors["lines"] = "This field is required."

    if not 0 < int(lines) < 100:
        errors["lines"] = "This field must be in the range of 0 to 100."

    return errors