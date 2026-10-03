from pprint import pprint
import psutil


def collect_thermal_metrics():
    thermals = {}
    thermals_sensors = psutil.sensors_temperatures()

    if not thermals_sensors:
        return thermals

    for hardware, sensors in thermals_sensors.items():
        thermals[hardware] = []

        for sensor in sensors:
            high_val = sensor.high if sensor.high is not None else 100
            crit_val = sensor.critical if sensor.critical is not None else 100

            thermals[hardware].append(
                {
                    "label": sensor.label or "Sensor",
                    "current": sensor.current,
                    "high": high_val if high_val < 100 else 100,
                    "critical": crit_val if high_val < 100 else 100,
                }
            )

    return thermals
