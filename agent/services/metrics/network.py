from typing import Any

import psutil


def collect_network_data() -> dict[str, int] | dict:
    networks_data = {}
    network_counters = psutil.net_io_counters(pernic=True)

    if not network_counters:
        return {}

    for network_name, network_data in network_counters.items():
        networks_data[network_name] = {
            "traffic_sent": network_data.bytes_sent,
            "traffic_recv": network_data.bytes_recv,
            "packets_sent": network_data.packets_sent,
            "packets_recv": network_data.packets_recv,
            "errin": network_data.errin,
            "errout": network_data.errout,
            "dropin": network_data.dropin,
            "dropout": network_data.dropout,
        }

    return networks_data
