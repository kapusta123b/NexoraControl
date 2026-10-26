"""Read-only Docker container and engine operations."""


def docker_ps(payload: dict) -> list[str]:
    command = ['docker', 'ps']
    if payload.get('--all', False):
        command.append('--all')
    if payload.get('--filter'):
        command.extend(['--filter', payload['--filter']])
    if payload.get('--size', False):
        command.append('--size')
    return command


def docker_ps_all(payload: dict) -> list[str]:
    return ['docker', 'ps', '--all']


def docker_logs(payload: dict) -> list[str]:
    command = ['docker', 'logs', '--tail', str(payload.get('lines', 100))]
    if payload.get('timestamps', False):
        command.append('--timestamps')
    if payload.get('since'):
        command.extend(['--since', payload['since']])
    command.append(payload['container'])
    return command


def docker_stats(payload: dict) -> list[str]:
    command = ['docker', 'stats', '--no-stream']
    if payload.get('--all', False):
        command.append('--all')
    return command


def docker_inspect(payload: dict) -> list[str]:
    return ['docker', 'container', 'inspect', payload['container']]


def docker_version(payload: dict) -> list[str]:
    return ['docker', 'version']


def docker_info(payload: dict) -> list[str]:
    return ['docker', 'info']


def docker_df(payload: dict) -> list[str]:
    return ['docker', 'system', 'df'] + (['--verbose'] if payload.get('verbose') else [])


def docker_container_top(payload: dict) -> list[str]:
    return ['docker', 'top', payload['container']]


def docker_container_port(payload: dict) -> list[str]:
    return ['docker', 'port', payload['container']]


def docker_container_diff(payload: dict) -> list[str]:
    return ['docker', 'diff', payload['container']]
