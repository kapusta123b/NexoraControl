"""Docker image metadata and bounded image download operations."""


def docker_images(payload: dict) -> list[str]:
    command = ['docker', 'images']
    if payload.get('--all', False):
        command.append('--all')
    if payload.get('--filter'):
        command.extend(['--filter', payload['--filter']])
    return command


def docker_image_inspect(payload: dict) -> list[str]:
    return ['docker', 'image', 'inspect', payload['image']]


def docker_image_history(payload: dict) -> list[str]:
    return ['docker', 'image', 'history', payload['image']]


def docker_image_pull(payload: dict) -> list[str]:
    return ['docker', 'image', 'pull', payload['image']]
