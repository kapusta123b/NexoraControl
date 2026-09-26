from .containers import *
from .information import *
from ..validators.docker import *

COMMAND_INFO_DOCKER = {
    "docker_ps": {"handler": docker_ps},
    "docker_ps_all": {"handler": docker_ps_all},
    "docker_logs": {"handler": docker_logs, "validator": docker_logs_validator},
    "docker_images": {"handler": docker_images},
    "docker_stats": {"handler": docker_stats},
    "docker_inspect": {
        "handler": docker_inspect,
        "validator": docker_inspect_validator,
    },
}

COMMAND_CONT_DOCKER = {
    "docker_stop_all_containers": {"handler": docker_stop_all_containers},
    "docker_restart_all_containers": {
        "handler": docker_restart_all_containers,
    },
}

COMMAND_DOCKER = COMMAND_CONT_DOCKER | COMMAND_INFO_DOCKER
