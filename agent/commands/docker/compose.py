"""Read-only Docker Compose operations with explicit compose file selection."""

def docker_compose_services(payload: dict) -> list[str]:
    return ['docker', 'compose', '-f', payload['compose_file'], 'config', '--services']


def docker_compose_ps(payload: dict) -> list[str]:
    cmd = ['docker', 'compose', '-f', payload['compose_file'], 'ps']
    if payload.get('--all', False):
        cmd.append('--all')
    return cmd


def docker_compose_logs(payload: dict) -> list[str]:
    cmd = ['docker', 'compose', '-f', payload['compose_file'], 'logs',
           '--no-color', '--tail', str(payload.get('lines', 100))]
    if payload.get('service'):
        cmd.append(payload['service'])
    return cmd
