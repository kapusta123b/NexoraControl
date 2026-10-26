"""Linux networking commands. Inputs are validated before forming argv."""


def network_interfaces(payload: dict) -> list[str]:
    return ["ip", "-brief", "address"]


def network_links(payload: dict) -> list[str]:
    return ["ip", "-brief", "link"]


def network_link_stats(payload: dict) -> list[str]:
    return ["ip", "-s", "link"]


def network_routes(payload: dict) -> list[str]:
    return ["ip", "-4", "route", "show"]


def network_listening(payload: dict) -> list[str]:
    return ["ss", "-tuln"]


def network_connections(payload: dict) -> list[str]:
    return ["ss", "-tuna"]


def network_socket_stats(payload: dict) -> list[str]:
    return ["ss", "-s"]


def network_neighbors(payload: dict) -> list[str]:
    return ["ip", "neigh", "show"]


def network_resolver(payload: dict) -> list[str]:
    return ["resolvectl", "status"]


def network_resolve_host(payload: dict) -> list[str]:
    return ["getent", "ahosts", payload["host"]]


def network_ping(payload: dict) -> list[str]:
    return [
        "ping",
        "-n",
        "-W",
        "2",
        "-c",
        str(payload.get("count", 3)),
        payload["host"],
    ]
