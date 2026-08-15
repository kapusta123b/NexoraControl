from .containers import *
from .information import *

COMMAND_DOCKER = {
    "docker_ps": docker_ps,
    "docker_ps_all": docker_ps_all,
    "docker_logs": docker_logs,
    "docker_images": docker_images,
    "docker_stats": docker_stats,
}