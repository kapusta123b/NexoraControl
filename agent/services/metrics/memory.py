import psutil

def collect_memory_metrics() -> dict:
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    return {
        "ram_load": memory.percent,
        "ram_used_bytes": memory.used,
        "ram_available_bytes": memory.available,
        "swap_used_bytes": swap.used,
        "swap_available_bytes": swap.free,
    }