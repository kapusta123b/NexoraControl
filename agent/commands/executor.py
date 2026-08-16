import subprocess


def subprocess_executor(command: list[str]) -> dict:
    try:
        result = subprocess.run(
            command,
            check=True,
            text=True,
            capture_output=True,
        )

        return {
            "status": "SUCCESS",
            "output": result.stdout.strip() or result.stderr.strip(),
        }

    except subprocess.CalledProcessError as e:
        error = (e.stderr or "").strip()

        return {
            "status": "FAILED",
            "output": error or f"Command finished with code {e.returncode}",
        }

    except FileNotFoundError as e:
        return {
            "status": "FAILED",
            "output": str(e),
        }

    except Exception as e:
        return {"status": "FAILED", "output": str(e)}
