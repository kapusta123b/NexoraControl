"""Docker-specific checks layered over the shared schema validator."""

from .common import validator_for

_docker_ps_schema = validator_for("docker_ps")
_docker_images_schema = validator_for("docker_images")

_CONTAINER_FILTERS = {
    "id",
    "name",
    "label",
    "exited",
    "status",
    "ancestor",
    "before",
    "since",
    "volume",
    "network",
    "publish",
    "expose",
    "health",
}
_IMAGE_FILTERS = {"dangling", "label", "before", "since", "reference", "until"}


def _filter_errors(payload: dict, schema_validator, keys: set[str]) -> dict:
    errors = schema_validator(payload)

    if errors or not isinstance(payload, dict):
        return errors

    value = payload.get("--filter")

    if value:
        filter_key = value.partition("=")[0]
        if filter_key not in keys:
            errors["--filter"] = "Unsupported Docker filter key."

    return errors


def docker_ps_validator(payload: dict) -> dict:
    return _filter_errors(payload, _docker_ps_schema, _CONTAINER_FILTERS)


def docker_images_validator(payload: dict) -> dict:
    return _filter_errors(payload, _docker_images_schema, _IMAGE_FILTERS)


docker_logs_validator = validator_for("docker_logs")
docker_inspect_validator = validator_for("docker_inspect")
