from commands.executor import subprocess_executor


def docker_ps(payload: dict) -> dict:
    return subprocess_executor(
        ["docker", "ps"],
    )


def docker_ps_all(payload: dict) -> dict:
    return subprocess_executor(
        ["docker", "ps", "-a"],
    )


def docker_logs(payload: dict) -> dict:
    container, lines = payload["container"], payload["lines"]

    return subprocess_executor(
        ["docker", "logs", "--tail", str(lines), str(container)],
    )


def docker_stats(payload: dict) -> dict:
    return subprocess_executor(
        ["docker", "stats", "--no-stream"],
    )


def docker_images(payload: dict) -> dict:
    return subprocess_executor(
        ["docker", "images", "-a"],
    )


def docker_inspect(payload: dict):
    container = payload.get("container")

    return subprocess_executor(
        ["docker", "inspect", str(container)],
    )
