from enum import StrEnum


class CommandRisk(StrEnum):
    SAFE = "safe"
    MODERATE = "moderate"
    DANGEROUS = "dangerous"


DOCKER_COMMANDS = {
    "Docker list": {
        "json_title": "docker_ps",
        "title": "List containers",
        "description": "List containers. Optionally include stopped containers, apply one "
        "filter, or show writable-layer sizes.",
        "risk": "safe",
        "fields": {
            "--all": {
                "type": "boolean",
                "description": "Include stopped containers",
                "required": False,
                "default": False,
            },
            "--filter": {
                "type": "string",
                "description": "Docker key=value filter, such as status=exited",
                "required": False,
                "placeholder": "status=exited",
                "pattern": "^[A-Za-z][A-Za-z0-9_-]{0,30}=.{1,160}$",
                "max_length": 180,
            },
            "--size": {
                "type": "boolean",
                "description": "Show container writable-layer sizes",
                "required": False,
                "default": False,
            },
        },
        "timeout": 12,
    },
    "Docker list (legacy all)": {
        "json_title": "docker_ps_all",
        "title": "List all containers",
        "description": "Legacy shortcut that lists all containers, including "
        "stopped ones.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Docker logs": {
        "json_title": "docker_logs",
        "title": "Container logs",
        "description": "Read a bounded number of recent log lines for a container.",
        "risk": "safe",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            },
            "lines": {
                "type": "integer",
                "description": "Maximum recent log lines",
                "required": False,
                "default": 100,
                "min": 1,
                "max": 500,
            },
            "timestamps": {
                "type": "boolean",
                "description": "Prefix log lines with timestamps",
                "required": False,
                "default": False,
            },
            "since": {
                "type": "string",
                "description": "Optional relative time window",
                "required": False,
                "placeholder": "1h",
                "pattern": "^\\d{1,5}[smhd]$",
            },
        },
        "timeout": 12,
    },
    "Docker stats": {
        "json_title": "docker_stats",
        "title": "Container resources",
        "description": "Collect one non-streaming CPU, memory and network snapshot.",
        "risk": "safe",
        "fields": {
            "--all": {
                "type": "boolean",
                "description": "Include stopped containers",
                "required": False,
                "default": False,
            }
        },
        "timeout": 25,
    },
    "Docker inspect": {
        "json_title": "docker_inspect",
        "title": "Inspect container",
        "description": "Show JSON metadata for one container.",
        "risk": "safe",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 12,
    },
    "Docker version": {
        "json_title": "docker_version",
        "title": "Docker version",
        "description": "Show Docker client and daemon versions.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Docker info": {
        "json_title": "docker_info",
        "title": "Docker engine information",
        "description": "Show daemon and runtime details.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Docker disk usage": {
        "json_title": "docker_df",
        "title": "Docker disk usage",
        "description": "Show space occupied by images, containers, cache and volumes.",
        "risk": "safe",
        "fields": {
            "verbose": {
                "type": "boolean",
                "description": "Show detailed per-object disk usage",
                "required": False,
                "default": False,
            }
        },
        "timeout": 12,
    },
    "Docker top": {
        "json_title": "docker_container_top",
        "title": "Container processes",
        "description": "Show processes running inside a container.",
        "risk": "safe",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 12,
    },
    "Docker ports": {
        "json_title": "docker_container_port",
        "title": "Container port mappings",
        "description": "Show published port mappings for a container.",
        "risk": "safe",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 12,
    },
    "Docker changes": {
        "json_title": "docker_container_diff",
        "title": "Container filesystem changes",
        "description": "List filesystem changes made by a container.",
        "risk": "safe",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 12,
    },
    "Docker start": {
        "json_title": "docker_container_start",
        "title": "Start container",
        "description": "Start one stopped container.",
        "risk": "moderate",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 90,
    },
    "Docker stop": {
        "json_title": "docker_container_stop",
        "title": "Stop container",
        "description": "Gracefully stop a selected container.",
        "risk": "dangerous",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            },
            "confirmation": {
                "type": "string",
                "description": "Confirm stopping the selected container",
                "required": True,
                "placeholder": "Type STOP to confirm",
                "must_equal": "STOP",
                "max_length": 32,
            },
        },
        "timeout": 90,
    },
    "Docker restart": {
        "json_title": "docker_container_restart",
        "title": "Restart container",
        "description": "Restart the selected container, interrupting its service.",
        "risk": "dangerous",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            },
            "confirmation": {
                "type": "string",
                "description": "Confirm restarting the selected " "container",
                "required": True,
                "placeholder": "Type RESTART to confirm",
                "must_equal": "RESTART",
                "max_length": 32,
            },
        },
        "timeout": 90,
    },
    "Docker pause": {
        "json_title": "docker_container_pause",
        "title": "Pause container",
        "description": "Pause all processes in a selected container.",
        "risk": "moderate",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 40,
    },
    "Docker unpause": {
        "json_title": "docker_container_unpause",
        "title": "Unpause container",
        "description": "Resume paused container processes.",
        "risk": "moderate",
        "fields": {
            "container": {
                "type": "string",
                "description": "Docker container name or ID",
                "required": True,
                "placeholder": "container",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 40,
    },
    "Docker stop all": {
        "json_title": "docker_stop_all_containers",
        "title": "Stop all containers",
        "description": "Stop every container on the host. Affects unrelated services.",
        "risk": "dangerous",
        "fields": {
            "confirmation": {
                "type": "string",
                "description": "Explicit confirmation for all " "containers",
                "required": True,
                "placeholder": "Type STOP_ALL to confirm",
                "must_equal": "STOP_ALL",
                "max_length": 32,
            }
        },
        "timeout": 180,
    },
    "Docker restart all": {
        "json_title": "docker_restart_all_containers",
        "title": "Restart all containers",
        "description": "Restart every container on the host. Affects unrelated "
        "services.",
        "risk": "dangerous",
        "fields": {
            "confirmation": {
                "type": "string",
                "description": "Explicit confirmation for all " "containers",
                "required": True,
                "placeholder": "Type RESTART_ALL to confirm",
                "must_equal": "RESTART_ALL",
                "max_length": 32,
            }
        },
        "timeout": 180,
    },
}


DOCKER_IMAGE_COMMANDS = {
    "Docker images": {
        "json_title": "docker_images",
        "title": "List Docker images",
        "description": "List local images.",
        "risk": "safe",
        "fields": {
            "--all": {
                "type": "boolean",
                "description": "Include intermediate and dangling images",
                "required": False,
                "default": False,
            },
            "--filter": {
                "type": "string",
                "description": "Docker key=value filter, such as " "dangling=true",
                "required": False,
                "placeholder": "dangling=true",
                "pattern": "^[A-Za-z][A-Za-z0-9_-]{0,30}=.{1,160}$",
                "max_length": 180,
            },
        },
        "timeout": 12,
    },
    "Docker image inspect": {
        "json_title": "docker_image_inspect",
        "title": "Inspect image",
        "description": "Read detailed metadata for a Docker image.",
        "risk": "safe",
        "fields": {
            "image": {
                "type": "string",
                "description": "Docker image name, tag, digest or ID",
                "required": True,
                "placeholder": "image",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:/@-]{0,254}$",
            }
        },
        "timeout": 12,
    },
    "Docker image history": {
        "json_title": "docker_image_history",
        "title": "Image history",
        "description": "Show the build layers of a Docker image.",
        "risk": "safe",
        "fields": {
            "image": {
                "type": "string",
                "description": "Docker image name, tag, digest or ID",
                "required": True,
                "placeholder": "image",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:/@-]{0,254}$",
            }
        },
        "timeout": 12,
    },
    "Docker image pull": {
        "json_title": "docker_image_pull",
        "title": "Pull image",
        "description": "Download an image to the host. Uses disk and network bandwidth.",
        "risk": "moderate",
        "fields": {
            "image": {
                "type": "string",
                "description": "Docker image name, tag, digest or ID",
                "required": True,
                "placeholder": "image",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.:/@-]{0,254}$",
            }
        },
        "timeout": 240,
    },
}


DOCKER_NETWORK_COMMANDS = {
    "Docker network list": {
        "json_title": "docker_network_ls",
        "title": "List Docker networks",
        "description": "List Docker networks on the host.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Docker network inspect": {
        "json_title": "docker_network_inspect",
        "title": "Inspect Docker network",
        "description": "Show configuration and attached containers.",
        "risk": "safe",
        "fields": {
            "network": {
                "type": "string",
                "description": "Docker network name or ID",
                "required": True,
                "placeholder": "network",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 12,
    },
}


DOCKER_VOLUME_COMMANDS = {
    "Docker volume list": {
        "json_title": "docker_volume_ls",
        "title": "List Docker volumes",
        "description": "List Docker volumes on the host.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Docker volume inspect": {
        "json_title": "docker_volume_inspect",
        "title": "Inspect Docker volume",
        "description": "Show metadata and mount paths for one volume.",
        "risk": "safe",
        "fields": {
            "volume": {
                "type": "string",
                "description": "Docker volume name",
                "required": True,
                "placeholder": "volume",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$",
            }
        },
        "timeout": 12,
    },
}


DOCKER_COMPOSE_COMMANDS = {
    "Compose services": {
        "json_title": "docker_compose_services",
        "title": "Compose services",
        "description": "List declared services in a Compose project.",
        "risk": "safe",
        "fields": {
            "compose_file": {
                "type": "string",
                "description": "Absolute path to a Compose YAML file",
                "required": True,
                "placeholder": "/srv/app/compose.yml",
                "pattern": "^/.{1,245}\\.ya?ml$",
                "max_length": 255,
            }
        },
        "timeout": 25,
    },
    "Compose containers": {
        "json_title": "docker_compose_ps",
        "title": "Compose containers",
        "description": "Show containers for a Compose project.",
        "risk": "safe",
        "fields": {
            "compose_file": {
                "type": "string",
                "description": "Absolute path to a Compose YAML " "file",
                "required": True,
                "placeholder": "/srv/app/compose.yml",
                "pattern": "^/.{1,245}\\.ya?ml$",
                "max_length": 255,
            },
            "--all": {
                "type": "boolean",
                "description": "Include stopped containers",
                "required": False,
                "default": False,
            },
        },
        "timeout": 25,
    },
    "Compose logs": {
        "json_title": "docker_compose_logs",
        "title": "Compose logs",
        "description": "Read bounded recent logs from a Compose project.",
        "risk": "safe",
        "fields": {
            "compose_file": {
                "type": "string",
                "description": "Absolute path to a Compose YAML file",
                "required": True,
                "placeholder": "/srv/app/compose.yml",
                "pattern": "^/.{1,245}\\.ya?ml$",
                "max_length": 255,
            },
            "lines": {
                "type": "integer",
                "description": "Maximum lines per service",
                "required": False,
                "default": 100,
                "min": 1,
                "max": 500,
            },
            "service": {
                "type": "string",
                "description": "Optional Compose service name",
                "required": False,
                "placeholder": "web",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.@-]{0,100}$",
                "max_length": 101,
            },
        },
        "timeout": 35,
    },
}


SYSTEM_COMMANDS = {
    "System uptime": {
        "json_title": "system_uptime",
        "title": "System uptime",
        "description": "Show how long the host has been running.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "OS information": {
        "json_title": "system_os_info",
        "title": "Operating system",
        "description": "Display Linux distribution and release information.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "CPU information": {
        "json_title": "system_cpu_info",
        "title": "CPU information",
        "description": "Display CPU architecture and hardware characteristics.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "RAM information": {
        "json_title": "system_ram_info",
        "title": "Memory information",
        "description": "Show memory and swap usage.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Disk overview (legacy)": {
        "json_title": "system_disk_info",
        "title": "Disk devices",
        "description": "List block devices and partitions.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Host name": {
        "json_title": "system_hostname",
        "title": "Hostname",
        "description": "Show the hostname assigned to the Linux system.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Kernel release": {
        "json_title": "system_kernel",
        "title": "Kernel version",
        "description": "Show the Linux kernel release.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Host date": {
        "json_title": "system_date",
        "title": "System date",
        "description": "Show the system clock in ISO-8601 format.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Load average": {
        "json_title": "system_load",
        "title": "Load averages",
        "description": "Show 1, 5 and 15 minute load averages.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Logged-in users": {
        "json_title": "system_users",
        "title": "Logged-in users",
        "description": "List current login sessions.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Last boot": {
        "json_title": "system_last_boot",
        "title": "Last boot time",
        "description": "Show the last system boot time.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Reboot host": {
        "json_title": "system_reboot",
        "title": "Reboot host",
        "description": "Reboot the entire Linux host, interrupting all services.",
        "risk": "dangerous",
        "fields": {
            "confirmation": {
                "type": "string",
                "description": "Type REBOOT to confirm this operation",
                "required": True,
                "placeholder": "Type REBOOT to confirm",
                "must_equal": "REBOOT",
                "max_length": 32,
            }
        },
        "timeout": 25,
    },
}


PROCESS_COMMANDS = {
    "Top processes": {
        "json_title": "system_processes",
        "title": "Top processes",
        "description": "List top processes by CPU or memory consumption.",
        "risk": "safe",
        "fields": {
            "lines": {
                "type": "integer",
                "description": "Maximum processes returned",
                "required": False,
                "default": 10,
                "min": 1,
                "max": 100,
            },
            "sort": {
                "type": "choice",
                "description": "Sort processes by resource utilization",
                "required": False,
                "choices": ["cpu", "memory"],
                "default": "cpu",
            },
        },
        "timeout": 20,
    },
    "Process details": {
        "json_title": "process_details",
        "title": "Process details",
        "description": "Inspect one process by PID.",
        "risk": "safe",
        "fields": {
            "pid": {
                "type": "integer",
                "description": "Process ID",
                "required": True,
                "min": 1,
                "max": 4194304,
            }
        },
        "timeout": 20,
    },
    "Process threads": {
        "json_title": "process_threads",
        "title": "Process threads",
        "description": "Show threads for one process.",
        "risk": "safe",
        "fields": {
            "pid": {
                "type": "integer",
                "description": "Process ID",
                "required": True,
                "min": 1,
                "max": 4194304,
            }
        },
        "timeout": 20,
    },
    "Process tree": {
        "json_title": "process_tree",
        "title": "Process tree",
        "description": "Show parent and child process relationships.",
        "risk": "safe",
        "fields": {},
        "timeout": 20,
    },
}


SERVICE_COMMANDS = {
    "Running services": {
        "json_title": "service_running",
        "title": "Running services",
        "description": "List running systemd services.",
        "risk": "safe",
        "fields": {},
        "timeout": 25,
    },
    "Failed services": {
        "json_title": "service_failed",
        "title": "Failed services",
        "description": "List failed systemd services.",
        "risk": "safe",
        "fields": {},
        "timeout": 25,
    },
    "Service status": {
        "json_title": "service_status",
        "title": "Service status",
        "description": "Show detailed status for one systemd unit.",
        "risk": "safe",
        "fields": {
            "service": {
                "type": "string",
                "description": "Systemd unit name, e.g. nginx.service",
                "required": True,
                "placeholder": "service",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.@-]{0,100}$",
            }
        },
        "timeout": 25,
    },
    "Service properties": {
        "json_title": "service_show",
        "title": "Service properties",
        "description": "Show key service properties such as state, PID and restart "
        "count.",
        "risk": "safe",
        "fields": {
            "service": {
                "type": "string",
                "description": "Systemd unit name, e.g. nginx.service",
                "required": True,
                "placeholder": "service",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.@-]{0,100}$",
            }
        },
        "timeout": 25,
    },
    "Service logs": {
        "json_title": "service_logs",
        "title": "Service journal",
        "description": "Show bounded recent systemd service logs.",
        "risk": "safe",
        "fields": {
            "service": {
                "type": "string",
                "description": "Systemd unit name, e.g. nginx.service",
                "required": True,
                "placeholder": "service",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.@-]{0,100}$",
            },
            "lines": {
                "type": "integer",
                "description": "Maximum journal entries",
                "required": False,
                "default": 50,
                "min": 1,
                "max": 250,
            },
        },
        "timeout": 30,
    },
    "Active timers": {
        "json_title": "service_timers",
        "title": "System timers",
        "description": "List systemd timers.",
        "risk": "safe",
        "fields": {},
        "timeout": 25,
    },
    "Restart service": {
        "json_title": "service_restart",
        "title": "Restart service",
        "description": "Restart a systemd service. This may interrupt users.",
        "risk": "dangerous",
        "fields": {
            "service": {
                "type": "string",
                "description": "Systemd unit name, e.g. nginx.service",
                "required": True,
                "placeholder": "service",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.@-]{0,100}$",
            },
            "confirmation": {
                "type": "string",
                "description": "Confirm restarting the systemd unit",
                "required": True,
                "placeholder": "Type RESTART_SERVICE to confirm",
                "must_equal": "RESTART_SERVICE",
                "max_length": 32,
            },
        },
        "timeout": 90,
    },
    "Start service": {
        "json_title": "service_start",
        "title": "Start service",
        "description": "Start a systemd service.",
        "risk": "moderate",
        "fields": {
            "service": {
                "type": "string",
                "description": "Systemd unit name, e.g. nginx.service",
                "required": True,
                "placeholder": "service",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.@-]{0,100}$",
            }
        },
        "timeout": 90,
    },
    "Stop service": {
        "json_title": "service_stop",
        "title": "Stop service",
        "description": "Stop a systemd service. This may interrupt users.",
        "risk": "dangerous",
        "fields": {
            "service": {
                "type": "string",
                "description": "Systemd unit name, e.g. nginx.service",
                "required": True,
                "placeholder": "service",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9_.@-]{0,100}$",
            },
            "confirmation": {
                "type": "string",
                "description": "Confirm stopping the systemd unit",
                "required": True,
                "placeholder": "Type STOP_SERVICE to confirm",
                "must_equal": "STOP_SERVICE",
                "max_length": 32,
            },
        },
        "timeout": 90,
    },
}


NETWORK_COMMANDS = {
    "IP interfaces": {
        "json_title": "network_interfaces",
        "title": "IP addresses",
        "description": "List IP addresses by interface.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Network links": {
        "json_title": "network_links",
        "title": "Network links",
        "description": "List link state and MAC addresses.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Interface counters": {
        "json_title": "network_link_stats",
        "title": "Interface counters",
        "description": "Show packet and error counters for interfaces.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Routes": {
        "json_title": "network_routes",
        "title": "Routing table",
        "description": "Display IPv4 routing information.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Listening ports": {
        "json_title": "network_listening",
        "title": "Listening sockets",
        "description": "Show locally listening TCP/UDP sockets.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "All connections": {
        "json_title": "network_connections",
        "title": "Socket connections",
        "description": "Display current TCP and UDP sockets.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Socket summary": {
        "json_title": "network_socket_stats",
        "title": "Socket statistics",
        "description": "Summarize socket counts and states.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "ARP neighbors": {
        "json_title": "network_neighbors",
        "title": "Neighbor cache",
        "description": "Show IP-to-link-layer neighbor entries.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Resolver status": {
        "json_title": "network_resolver",
        "title": "DNS resolver",
        "description": "Display DNS resolver configuration.",
        "risk": "safe",
        "fields": {},
        "timeout": 20,
    },
    "Resolve hostname": {
        "json_title": "network_resolve_host",
        "title": "DNS lookup",
        "description": "Resolve a hostname using the system resolver.",
        "risk": "safe",
        "fields": {
            "host": {
                "type": "string",
                "description": "Hostname or IP address",
                "required": True,
                "placeholder": "host",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9.:-]{0,252}$",
                "max_length": 253,
            }
        },
        "timeout": 20,
    },
    "Ping host": {
        "json_title": "network_ping",
        "title": "Ping destination",
        "description": "Send a few ICMP requests to a destination.",
        "risk": "safe",
        "fields": {
            "host": {
                "type": "string",
                "description": "Hostname or IP address",
                "required": True,
                "placeholder": "host",
                "pattern": "^[A-Za-z0-9][A-Za-z0-9.:-]{0,252}$",
                "max_length": 253,
            },
            "count": {
                "type": "integer",
                "description": "ICMP request count",
                "required": False,
                "default": 3,
                "min": 1,
                "max": 5,
            },
        },
        "timeout": 20,
    },
}


STORAGE_COMMANDS = {
    "Disk usage": {
        "json_title": "storage_df",
        "title": "Filesystem usage",
        "description": "Show capacity and available disk space.",
        "risk": "safe",
        "fields": {
            "path": {
                "type": "string",
                "description": "Absolute filesystem path",
                "required": False,
                "default": "/",
                "placeholder": "/",
                "pattern": "^/.{0,254}$",
                "max_length": 255,
            }
        },
        "timeout": 12,
    },
    "Inodes": {
        "json_title": "storage_inodes",
        "title": "Filesystem inodes",
        "description": "Show filesystem inode usage.",
        "risk": "safe",
        "fields": {
            "path": {
                "type": "string",
                "description": "Absolute filesystem path",
                "required": False,
                "default": "/",
                "placeholder": "/",
                "pattern": "^/.{0,254}$",
                "max_length": 255,
            }
        },
        "timeout": 12,
    },
    "Block devices": {
        "json_title": "storage_lsblk",
        "title": "Block devices",
        "description": "List disks, partitions, filesystems and mount points.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Mount points": {
        "json_title": "storage_mounts",
        "title": "Mounted filesystems",
        "description": "Show filesystems mounted on the host.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Swap devices": {
        "json_title": "storage_swap",
        "title": "Swap devices",
        "description": "Show swap areas and utilization.",
        "risk": "safe",
        "fields": {},
        "timeout": 12,
    },
    "Directory size": {
        "json_title": "storage_du",
        "title": "Directory disk usage",
        "description": "Calculate disk usage for a selected directory.",
        "risk": "safe",
        "fields": {
            "path": {
                "type": "string",
                "description": "Absolute directory path",
                "required": True,
                "placeholder": "path",
                "pattern": "^/.{0,254}$",
                "max_length": 255,
            }
        },
        "timeout": 60,
    },
    "Filesystem metadata": {
        "json_title": "storage_stat",
        "title": "Filesystem metadata",
        "description": "Show filesystem type and block statistics.",
        "risk": "safe",
        "fields": {
            "path": {
                "type": "string",
                "description": "Absolute filesystem path",
                "required": False,
                "default": "/",
                "placeholder": "/",
                "pattern": "^/.{0,254}$",
                "max_length": 255,
            }
        },
        "timeout": 12,
    },
}


DIAGNOSTICS_COMMANDS = {
    "Journal errors": {
        "json_title": "diag_journal_errors",
        "title": "Recent journal errors",
        "description": "Display recent error-level system journal entries.",
        "risk": "safe",
        "fields": {
            "lines": {
                "type": "integer",
                "description": "Maximum entries",
                "required": False,
                "default": 50,
                "min": 1,
                "max": 250,
            }
        },
        "timeout": 30,
    },
    "Kernel messages": {
        "json_title": "diag_kernel_logs",
        "title": "Kernel messages",
        "description": "Display recent kernel messages from the journal.",
        "risk": "safe",
        "fields": {
            "lines": {
                "type": "integer",
                "description": "Maximum entries",
                "required": False,
                "default": 50,
                "min": 1,
                "max": 250,
            }
        },
        "timeout": 30,
    },
    "Boot journal errors": {
        "json_title": "diag_boot_errors",
        "title": "Current boot errors",
        "description": "List errors from the current system boot.",
        "risk": "safe",
        "fields": {
            "lines": {
                "type": "integer",
                "description": "Maximum entries",
                "required": False,
                "default": 50,
                "min": 1,
                "max": 250,
            }
        },
        "timeout": 30,
    },
    "Failed units": {
        "json_title": "diag_failed_units",
        "title": "Failed systemd units",
        "description": "List failed services and other units.",
        "risk": "safe",
        "fields": {},
        "timeout": 25,
    },
    "Boot performance": {
        "json_title": "diag_boot_time",
        "title": "Boot performance",
        "description": "Show systemd boot-time summary.",
        "risk": "safe",
        "fields": {},
        "timeout": 25,
    },
    "Time synchronization": {
        "json_title": "diag_time_sync",
        "title": "Time synchronization",
        "description": "Show NTP and timezone synchronization information.",
        "risk": "safe",
        "fields": {},
        "timeout": 25,
    },
    "Virtualization": {
        "json_title": "diag_virtualization",
        "title": "Virtualization type",
        "description": "Identify the virtualization technology, if any.",
        "risk": "safe",
        "fields": {},
        "timeout": 20,
    },
    "Journal space": {
        "json_title": "diag_journal_disk",
        "title": "Journal disk usage",
        "description": "Show disk usage of the systemd journal.",
        "risk": "safe",
        "fields": {},
        "timeout": 20,
    },
    "Boot history": {
        "json_title": "diag_boot_history",
        "title": "Boot history",
        "description": "List journal-recorded system boots.",
        "risk": "safe",
        "fields": {},
        "timeout": 25,
    },
}


CUSTOM_COMMANDS = {}


COMMANDS_REGISTRY = {
    "Docker": DOCKER_COMMANDS,
    "Docker Images": DOCKER_IMAGE_COMMANDS,
    "Docker Networks": DOCKER_NETWORK_COMMANDS,
    "Docker Volumes": DOCKER_VOLUME_COMMANDS,
    "Docker Compose": DOCKER_COMPOSE_COMMANDS,
    "System": SYSTEM_COMMANDS,
    "Processes": PROCESS_COMMANDS,
    "Services": SERVICE_COMMANDS,
    "Network": NETWORK_COMMANDS,
    "Storage": STORAGE_COMMANDS,
    "Diagnostics": DIAGNOSTICS_COMMANDS,
    "Custom": CUSTOM_COMMANDS,
}

COMMANDS_BY_ID = {
    entry["json_title"]: entry
    for category in COMMANDS_REGISTRY.values()
    for entry in category.values()
}
