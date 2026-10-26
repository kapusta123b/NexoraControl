"""Linux system, process, service, networking and diagnostics registries."""

from commands.registry_helpers import register_handlers
from commands.validators.system import service_validator_for
from . import system, processes, services, network, storage, diagnostics
from .output_parser import system_cpu_info_output, system_processes_output

COMMAND_HOST_SYSTEM = register_handlers(
    system,
    [
        "system_uptime",
        "system_os_info",
        "system_cpu_info",
        "system_ram_info",
        "system_disk_info",
        "system_hostname",
        "system_kernel",
        "system_date",
        "system_load",
        "system_users",
        "system_last_boot",
        "system_reboot",
    ],
    {"system_cpu_info": system_cpu_info_output},
)
COMMAND_PROCESSES = register_handlers(
    processes,
    [
        "system_processes",
        "process_details",
        "process_threads",
        "process_tree",
    ],
    {"system_processes": system_processes_output},
)
COMMAND_SERVICES = register_handlers(
    services,
    [
        "service_running",
        "service_failed",
        "service_status",
        "service_show",
        "service_logs",
        "service_timers",
        "service_restart",
        "service_start",
        "service_stop",
    ],
)
COMMAND_NETWORK = register_handlers(
    network,
    [
        "network_interfaces",
        "network_links",
        "network_link_stats",
        "network_routes",
        "network_listening",
        "network_connections",
        "network_socket_stats",
        "network_neighbors",
        "network_resolver",
        "network_resolve_host",
        "network_ping",
    ],
)
COMMAND_STORAGE = register_handlers(
    storage,
    [
        "storage_df",
        "storage_inodes",
        "storage_lsblk",
        "storage_mounts",
        "storage_swap",
        "storage_du",
        "storage_stat",
    ],
)
COMMAND_DIAGNOSTICS = register_handlers(
    diagnostics,
    [
        "diag_journal_errors",
        "diag_kernel_logs",
        "diag_boot_errors",
        "diag_failed_units",
        "diag_boot_time",
        "diag_time_sync",
        "diag_virtualization",
        "diag_journal_disk",
        "diag_boot_history",
    ],
)
COMMAND_SYSTEM = (
    COMMAND_HOST_SYSTEM
    | COMMAND_PROCESSES
    | COMMAND_SERVICES
    | COMMAND_NETWORK
    | COMMAND_STORAGE
    | COMMAND_DIAGNOSTICS
)

# Service names cannot target non-service systemd units.
for _command_name, _definition in COMMAND_SERVICES.items():
    if _command_name in {
        "service_status",
        "service_show",
        "service_logs",
        "service_start",
        "service_stop",
        "service_restart",
    }:
        _definition["validator"] = service_validator_for(_command_name)
