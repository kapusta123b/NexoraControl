import subprocess


def docker_container_start(payload: dict) -> list[str]:
    return ["docker", "start", payload["container"]]


def docker_container_stop(payload: dict) -> list[str]:
    return ["docker", "stop", payload["container"]]


def docker_container_restart(payload: dict) -> list[str]:
    return ["docker", "restart", payload["container"]]


def docker_container_pause(payload: dict) -> list[str]:
    return ["docker", "pause", payload["container"]]


def docker_container_unpause(payload: dict) -> list[str]:
    return ["docker", "unpause", payload["container"]]


def _get_all_containers() -> list[str]:
    """Resolve running container IDs on the agent, not the desktop."""
    result = subprocess.run(
        ["docker", "ps", "-q"],
        check=True,
        capture_output=True,
        text=True,
        timeout=15,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def docker_stop_all_containers(payload: dict) -> list[str]:
    ids = _get_all_containers()
    return ["docker", "stop", *ids] if ids else ["docker", "ps", "-q"]


def docker_restart_all_containers(payload: dict) -> list[str]:
    ids = _get_all_containers()
    return ["docker", "restart", *ids] if ids else ["docker", "ps", "-q"]
