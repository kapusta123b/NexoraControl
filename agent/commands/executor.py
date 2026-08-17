import subprocess


def subprocess_executor(command: list[str], timeout: int) -> dict:
    try:
        result = subprocess.run(
            command,
            check=True,
            text=True,
            capture_output=True,
            timeout=timeout,
        )

        if not result.stderr and not result.stdout:
            return {
                "status": "FAILED",
                "errors": {"Executor": "Command return None!"},
            }

        return {
            "status": "SUCCESS",
            "output": result.stdout.strip() or result.stderr.strip(),
        }

    except subprocess.CalledProcessError as e:
        error = (e.stderr or e.stdout or "").strip()

        return {
            "status": "FAILED",
            "output": error or f"Command finished with code {e.returncode}",
        }

    except subprocess.TimeoutExpired:
        return {
            "status": "FAILED",
            "output": f"Command timed out after {timeout} seconds",
        }

    except FileNotFoundError as e:
        return {
            "status": "FAILED",
            "output": str(e),
        }

    except Exception as e:
        return {
            "status": "FAILED",
            "output": str(e),
        }
