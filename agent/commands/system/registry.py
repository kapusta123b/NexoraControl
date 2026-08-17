from .system import *
from ..validators.system import *
from .output_parser import *

COMMAND_SYSTEM = {
    "system_uptime": {"handler": system_uptime},
    "system_os_info": {"handler": system_os_info},
    "system_cpu_info": {
        "handler": system_cpu_info,
        "output_parser": system_cpu_info_output,
    },
    "system_ram_info": {"handler": system_ram_info},
    "system_disk_info": {"handler": system_disk_info},
    "system_processes": {
        "handler": system_processes,
        "validator": system_processes_validator,
        "output_parser": system_processes_output,
    },
    "system_reboot": {"handler": system_reboot},
}
