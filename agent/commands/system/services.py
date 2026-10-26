"""systemd inspections and opt-in service lifecycle operations."""

def service_running(payload: dict) -> list[str]:
    return ['systemctl', 'list-units', '--type=service', '--state=running', '--no-pager', '--plain']

def service_failed(payload: dict) -> list[str]:
    return ['systemctl', 'list-units', '--type=service', '--state=failed', '--no-pager', '--plain']

def service_status(payload: dict) -> list[str]:
    return ['systemctl', '--no-pager', '--full', 'status', payload['service']]

def service_show(payload: dict) -> list[str]:
    return ['systemctl', 'show', payload['service'],
            '--property=Id,Description,ActiveState,SubState,MainPID,NRestarts,UnitFileState']

def service_logs(payload: dict) -> list[str]:
    return ['journalctl', '--no-pager', '-u', payload['service'], '-n', str(payload.get('lines', 50))]

def service_timers(payload: dict) -> list[str]:
    return ['systemctl', 'list-timers', '--all', '--no-pager']

def service_restart(payload: dict) -> list[str]:
    return ['systemctl', 'restart', payload['service']]

def service_start(payload: dict) -> list[str]:
    return ['systemctl', 'start', payload['service']]

def service_stop(payload: dict) -> list[str]:
    return ['systemctl', 'stop', payload['service']]
