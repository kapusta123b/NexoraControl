"""Linux system information and explicit host reboot."""

def system_uptime(payload: dict) -> list[str]: return ['uptime', '-p']
def system_os_info(payload: dict) -> list[str]: return ['cat', '/etc/os-release']
def system_cpu_info(payload: dict) -> list[str]: return ['lscpu']
def system_ram_info(payload: dict) -> list[str]: return ['free', '-h']
def system_disk_info(payload: dict) -> list[str]: return ['lsblk']
def system_hostname(payload: dict) -> list[str]: return ['hostname']
def system_kernel(payload: dict) -> list[str]: return ['uname', '-r']
def system_date(payload: dict) -> list[str]: return ['date', '--iso-8601=seconds']
def system_load(payload: dict) -> list[str]: return ['uptime']
def system_users(payload: dict) -> list[str]: return ['who']
def system_last_boot(payload: dict) -> list[str]: return ['who', '-b']
def system_reboot(payload: dict) -> list[str]: return ['systemctl', 'reboot']
