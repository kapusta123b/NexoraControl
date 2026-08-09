import subprocess


def system_uptime(payload: dict) -> dict:
    uptime = subprocess.run(
        ["uptime", "-p"], capture_output=True, text=True
    ).stdout.strip()

    return {"status": "SUCCESS", "output": uptime}
