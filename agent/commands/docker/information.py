import subprocess


def docker_ps(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["docker", "ps"],
            check=True,
            text=True,
            capture_output=True,
        )
        return {"status": "SUCCESS", "output": result.stdout}

    except Exception as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}


def docker_ps_all(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["docker", "ps" "-al"],
            check=True,
            text=True,
            capture_output=True,
        )
        return {"status": "SUCCESS", "output": result.stdout}

    except Exception as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}


def docker_logs(payload: dict) -> dict:

    try:
        container, lines = payload.get("container"), payload.get("lines", 20)
        result = subprocess.run(
            ["docker", "logs", container, "-n", lines],
            check=True,
            text=True,
            capture_output=True,
        )
        return {"status": "SUCCESS", "output": result.stdout}

    except Exception as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}


def docker_stats(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["docker", "stats"],
            check=True,
            text=True,
            capture_output=True,
        )
        return {"status": "SUCCESS", "output": result.stdout}

    except Exception as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}


def docker_images(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["docker", "images", "-a"],
            check=True,
            text=True,
            capture_output=True,
        )
        return {"status": "SUCCESS", "output": result.stdout}

    except Exception as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}
