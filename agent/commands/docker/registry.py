from .containers import *
from .information import *
from ..validators.docker import *

COMMAND_DOCKER = {
    "docker_ps": docker_ps,
    "docker_ps_all": docker_ps_all,
    "docker_logs": (docker_logs, docker_logs_validator),
    "docker_images": docker_images,
    "docker_stats": docker_stats,
    "docker_inspect": (docker_inspect, docker_inspect_validator),
}
