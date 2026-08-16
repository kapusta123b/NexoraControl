def docker_logs_validator(payload: dict) -> dict:
    errors = {}

    container, lines = payload.get("container"), payload.get("lines")

    if not container:
        errors["container"] = "This field is required."

    if not lines:
        errors["lines"] = "This field is required."

        return errors
    
    if not 0 < int(lines) < 500:
        errors["lines"] = "This field must be in the range of 0 to 500."

    return errors


def docker_inspect_validator(payload: dict) -> dict:
    errors = {}

    container = payload.get("container")

    if not container:
        errors["container"] = "This field is required."

    return errors
