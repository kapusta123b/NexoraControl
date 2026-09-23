import psutil


def _collect_storage_data() -> dict:
    disks = {}

    disks_partitions = psutil.disk_partitions()
    disks_statistics = psutil.disk_io_counters(perdisk=True)

    if disks_statistics:
        for disk_name, disk_info in disks_statistics.items():

            if disk_info.read_bytes and disk_info.write_bytes:
                disk_dict = {
                    disk_name: {
                        "read_bytes": disk_info.read_bytes,
                        "write_bytes": disk_info.write_bytes,
                    }
                }

                disks.update(**disk_dict)

                for disk_part in disks_partitions:
                    if disk_part.device.replace("/dev/", "") == disk_name:
                        disk_usage = psutil.disk_usage(disk_part.mountpoint)

                        disks[disk_name]["mount"] = disk_part.mountpoint
                        disks[disk_name]["fstype"] = disk_part.fstype
                        
                        disks[disk_name]["used"] = disk_usage.used
                        disks[disk_name]["free"] = disk_usage.free
                        disks[disk_name]["percent"] = disk_usage.percent

    return disks
