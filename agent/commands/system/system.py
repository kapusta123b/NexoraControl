from commands.executor import subprocess_executor


def system_uptime(payload: dict) -> dict:
    return subprocess_executor(["uptime", "-p"])


def system_os_info(payload: dict) -> dict:
    return subprocess_executor(["cat", "/etc/os-release"])


def system_cpu_info(payload: dict) -> dict:
    result = subprocess_executor(["lscpu"])

    trimmed_lines = []
    for line in result.get("output"):
        trimmed_lines.append(line)
        if "BogoMIPS" in line:
            break

    output_text = "\n".join(trimmed_lines)
    result["output"] = output_text

    return result


def system_ram_info(payload: dict) -> dict:
    return subprocess_executor(
        ["free", "-h"],
    )


def system_disk_info(payload: dict) -> dict:
    return subprocess_executor(
        ["lsblk"],
    )


def system_processes(payload: dict) -> dict:
    displayed_lines = payload["lines"]

    result = subprocess_executor(
        ["ps", "-eo", "pid,ppid,%cpu,%mem,comm", "--sort=-%cpu"],
    )

    lines = result.split("\n")
    limited_output = "\n".join(lines[: displayed_lines + 1])

    result["output"] = limited_output
    return result


def system_reboot(payload: dict) -> dict:
    return subprocess_executor(
        ["systemctl", "reboot"],
    )
