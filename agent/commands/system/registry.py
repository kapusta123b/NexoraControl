from .system import *
from ..validators.system import *

COMMAND_SYSTEM = {
    "system_uptime": system_uptime,
    "system_os_info": system_os_info,
    "system_cpu_info": system_cpu_info,
    "system_ram_info": system_ram_info,
    "system_disk_info": system_disk_info,
    "system_processes": (system_processes, system_processes_validator),
    "system_reboot": system_reboot,
}
