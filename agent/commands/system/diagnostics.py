"""Read-only troubleshooting commands suitable for a short-running agent."""

def diag_journal_errors(payload: dict) -> list[str]:
    return ['journalctl', '--no-pager', '-p', 'err', '-n', str(payload.get('lines', 50))]

def diag_kernel_logs(payload: dict) -> list[str]:
    return ['journalctl', '--no-pager', '-k', '-n', str(payload.get('lines', 50))]

def diag_boot_errors(payload: dict) -> list[str]:
    return ['journalctl', '--no-pager', '-b', '-p', 'err', '-n', str(payload.get('lines', 50))]

def diag_failed_units(payload: dict) -> list[str]:
    return ['systemctl', '--failed', '--no-pager']

def diag_boot_time(payload: dict) -> list[str]: return ['systemd-analyze', 'time']
def diag_time_sync(payload: dict) -> list[str]: return ['timedatectl', 'status']
def diag_virtualization(payload: dict) -> list[str]: return ['systemd-detect-virt']
def diag_journal_disk(payload: dict) -> list[str]: return ['journalctl', '--disk-usage']
def diag_boot_history(payload: dict) -> list[str]: return ['journalctl', '--list-boots', '--no-pager']
