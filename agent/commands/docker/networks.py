"""Read-only Docker networking operations."""

def docker_network_ls(payload: dict) -> list[str]:
    return ['docker', 'network', 'ls']


def docker_network_inspect(payload: dict) -> list[str]:
    return ['docker', 'network', 'inspect', payload['network']]
