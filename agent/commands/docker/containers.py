import subprocess


def _get_all_containers() -> list[str]:
    try:
        res = subprocess.check_output(["docker", "ps", "-a", "-q"], text=True)
        container_ids = [cid.strip() for cid in res.splitlines() if cid.strip()]
        return container_ids
    except subprocess.CalledProcessError:
        return []


def docker_stop_all_containers(payload: dict) -> list:
    container_ids = _get_all_containers()
    if not container_ids:
        return []

    return ["docker", "stop"] + container_ids


def docker_restart_all_containers(payload: dict) -> list:
    container_ids = _get_all_containers()
    if not container_ids:
        return []

    return ["docker", "restart"] + container_ids
