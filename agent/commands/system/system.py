def system_uptime(payload: dict) -> list:
    return ["uptime", "-p"]


def system_os_info(payload: dict) -> list:
    return ["cat", "/etc/os-release"]


def system_cpu_info(payload: dict) -> list:
    return ["lscpu"]


def system_ram_info(payload: dict) -> list:
    return ["free", "-h"]


def system_disk_info(payload: dict) -> list:
    return ["lsblk"]


def system_processes(payload: dict) -> list:
    limit = payload.get("limit", 5)

    bash_script = (
        f"ps -eo comm,%cpu,%mem,state --no-headers --sort=-%cpu | head -n {limit}"
    )

    return ["bash", "-c", bash_script]


def system_reboot(payload: dict) -> list:
    return ["systemctl", "reboot"]
