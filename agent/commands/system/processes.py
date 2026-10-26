"""Read-only process inspection. No shell pipelines or string interpolation."""

def system_processes(payload: dict) -> list[str]:
    sort = '-%mem' if payload.get('sort') == 'memory' else '-%cpu'
    return ['ps', '-eo', 'pid,comm,%cpu,%mem,state', '--sort=' + sort]


def process_details(payload: dict) -> list[str]:
    return ['ps', '-p', str(payload['pid']), '-o', 'pid,ppid,user,comm,%cpu,%mem,state,etime']


def process_threads(payload: dict) -> list[str]:
    return ['ps', '-L', '-p', str(payload['pid']), '-o', 'pid,tid,comm,%cpu,state']


def process_tree(payload: dict) -> list[str]:
    return ['pstree', '-p']
