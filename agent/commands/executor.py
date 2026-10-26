import subprocess

MAX_OUTPUT_CHARS = 9_200


def _limit(text: str) -> str:
    if len(text) <= MAX_OUTPUT_CHARS:
        return text

    return text[:MAX_OUTPUT_CHARS] + "\n[Output truncated by NexoraControl]"


def subprocess_executor(command: list[str], timeout: int) -> dict:
    if (
        not isinstance(command, list)
        or not command
        or not all(isinstance(arg, str) for arg in command)
    ):
        return {
            "status": "FAILED",
            "errors": {"command": "Invalid command arguments."},
            "output": "",
        }
    try:
        result = subprocess.run(
            command,
            check=False,
            text=True,
            capture_output=True,
            timeout=timeout,
            shell=False,
        )

        stdout = (result.stdout or "").strip()
        stderr = (result.stderr or "").strip()
        if result.returncode == 0:
            return {"status": "SUCCESS", "output": _limit(stdout or stderr)}

        return {
            "status": "FAILED",
            "output": _limit(
                stderr or stdout or f"Command exited with code {result.returncode}"
            ),
            "errors": {"exit_code": result.returncode},
        }
    except subprocess.TimeoutExpired:
        return {
            "status": "FAILED",
            "output": f"Command timed out after {timeout} seconds",
        }
    except FileNotFoundError as error:
        return {"status": "FAILED", "output": f"Utility unavailable: {error.filename}"}

    except OSError as error:
        return {"status": "FAILED", "output": f"Unable to start command: {error}"}
