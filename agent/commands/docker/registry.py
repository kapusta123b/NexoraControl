"""Docker commands organized by function, independent of desktop UI categories."""
from commands.registry_helpers import register_handlers
from commands.validators.docker import docker_ps_validator, docker_images_validator
from . import information, containers, images, networks, volumes, compose

COMMAND_INFO_DOCKER = register_handlers(information, [
    'docker_ps','docker_ps_all','docker_logs','docker_stats','docker_inspect',
    'docker_version','docker_info','docker_df','docker_container_top',
    'docker_container_port','docker_container_diff',
])
COMMAND_CONT_DOCKER = register_handlers(containers, [
    'docker_container_start','docker_container_stop','docker_container_restart',
    'docker_container_pause','docker_container_unpause',
    'docker_stop_all_containers','docker_restart_all_containers',
])
COMMAND_IMAGE_DOCKER = register_handlers(images, [
    'docker_images','docker_image_inspect','docker_image_history','docker_image_pull',
])
COMMAND_NETWORK_DOCKER = register_handlers(networks, [
    'docker_network_ls','docker_network_inspect',
])
COMMAND_VOLUME_DOCKER = register_handlers(volumes, [
    'docker_volume_ls','docker_volume_inspect',
])
COMMAND_COMPOSE_DOCKER = register_handlers(compose, [
    'docker_compose_services','docker_compose_ps','docker_compose_logs',
])
COMMAND_DOCKER = (
    COMMAND_INFO_DOCKER | COMMAND_CONT_DOCKER | COMMAND_IMAGE_DOCKER
    | COMMAND_NETWORK_DOCKER | COMMAND_VOLUME_DOCKER | COMMAND_COMPOSE_DOCKER
)

# Filter key checks supplement type/range validation.
COMMAND_INFO_DOCKER['docker_ps']['validator'] = docker_ps_validator
COMMAND_IMAGE_DOCKER['docker_images']['validator'] = docker_images_validator
