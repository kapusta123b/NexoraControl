import psutil


def _collect_cpu_metrics() -> dict:
    load_average = psutil.getloadavg()

    return {
        "cpu_load": psutil.cpu_percent(interval=1),
        "cpu_load_per_core": psutil.cpu_percent(percpu=True),
        "load_average": [load_average[0], load_average[1], load_average[2]],
    }
