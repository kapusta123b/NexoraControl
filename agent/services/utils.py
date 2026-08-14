import subprocess


def get_system_hostname() -> str:
    name = subprocess.run("hostname", capture_output=True, text=True).stdout.strip()

    return name