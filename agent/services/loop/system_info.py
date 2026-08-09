import psutil


def _get_system_info() -> dict:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    return {"cpu_load": round(cpu), "ram_load": round(ram)}
