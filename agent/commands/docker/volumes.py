"""Read-only Docker volume operations."""

def docker_volume_ls(payload: dict) -> list[str]:
    return ['docker', 'volume', 'ls']


def docker_volume_inspect(payload: dict) -> list[str]:
    return ['docker', 'volume', 'inspect', payload['volume']]
