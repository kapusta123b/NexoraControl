import psutil

import json
import subprocess


def _get_table_drives() -> list[dict]:
    cmd = ["lsblk", "-d", "-J", "-o", "NAME,MODEL,TRAN,SIZE,ROTA,STATE"]
    res = subprocess.check_output(cmd, text=True)
    devices = json.loads(res).get("blockdevices", [])

    table_data = []

    for dev in devices:
        name = dev["name"]

        if "loop" in name:
            continue

        is_ssd = dev.get("rota") == 0
        is_nvme = "nvme" in name or dev.get("tran") == "nvme"

        if is_nvme:
            drive_type = "NVMe SSD"
        else:
            drive_type = "SATA SSD" if is_ssd else "SATA HDD"

        status = (dev.get("state") or "ONLINE").upper()

        model_name = dev.get("model")
        model = model_name.strip() if model_name else "Generic Drive"

        table_data.append(
            {
                "device": name,
                "model": model,
                "type": drive_type,
                "capacity": dev.get("size", "N/A"),
                "status": status,
            }
        )

    return table_data


def collect_storage_data() -> dict:
    disks = {}

    disks_partitions = psutil.disk_partitions()
    disks_statistics = psutil.disk_io_counters(perdisk=True)

    if disks_statistics:
        for disk_name, disk_info in disks_statistics.items():
            if "loop" in disk_name:
                continue

            if ("p" in disk_name and disk_name[-1].isdigit()) or (
                disk_name.startswith("sd") and disk_name[-1].isdigit()
            ):
                continue

            disks[disk_name] = {
                "read_bytes": disk_info.read_bytes,
                "write_bytes": disk_info.write_bytes,
                "read_count": disk_info.read_count,
                "write_count": disk_info.write_count,
            }

        drives_info: list[dict] = _get_table_drives()

        for drive_info in drives_info:
            device_name = drive_info["device"]

            if device_name in disks:
                drive_info.pop("device")
                disks[device_name].update(drive_info)

    for disk_part in disks_partitions:
        if "loop" in disk_part.device:
            continue

        try:
            disk_usage = psutil.disk_usage(disk_part.mountpoint)
            part_name = disk_part.device.replace("/dev/", "")

            disks[part_name] = {
                "mount": disk_part.mountpoint,
                "fstype": disk_part.fstype,
                "used": disk_usage.used,
                "free": disk_usage.free,
                "percent": disk_usage.percent,
            }

        except PermissionError:
            continue

    return disks
