def docker_stop_all_containers(payload: dict) -> list:
    return ["docker", "stop", "$(docker ps -a -q)"]

def docker_restart_all_containers(payload: dict) -> list:
    return ["docker", "restart", "$(docker ps -a -q)"]
