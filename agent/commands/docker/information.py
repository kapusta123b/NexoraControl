def docker_ps(payload: dict) -> list:
    return ["docker", "ps"]


def docker_ps_all(payload: dict) -> list:
    return ["docker", "ps", "-a"]


def docker_logs(payload: dict) -> list:
    container, lines = payload["container"], payload["lines"]

    return ["docker", "logs", "--tail", str(lines), str(container)]


def docker_stats(payload: dict) -> list:
    return ["docker", "stats", "--no-stream"]


def docker_images(payload: dict) -> list:
    return ["docker", "images", "-a"]


def docker_inspect(payload: dict):
    container = payload.get("container")

    return ["docker", "inspect", str(container)]
