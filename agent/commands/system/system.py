import subprocess


def system_uptime(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["uptime", "-p"], capture_output=True, text=True, check=True
        )
        return {"status": "SUCCESS", "output": result.stdout.strip()}

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() or f"The command finished with code {e.returncode}"
        return {"status": "FAILED", "output": error_msg}

    except Exception as e:
        return {"status": "FAILED", "output": str(e)}