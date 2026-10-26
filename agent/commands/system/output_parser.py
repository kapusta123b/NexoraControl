"""Output adapters for human-friendly command results."""


def system_cpu_info_output(result: dict, payload: dict) -> dict:
    """Return full lscpu output; no fragile locale-dependent BogoMIPS cutoff."""
    return result


def system_processes_output(result: dict, payload: dict) -> dict:
    """Keep the ps header and up to N process rows."""
    lines = result.get('output', '').splitlines()
    limit = payload.get('lines', 10)
    result['output'] = '\n'.join(lines[:limit + 1])
    return result
