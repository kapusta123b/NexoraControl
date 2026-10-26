"""Linux disk and filesystem inspection operations."""


def storage_df(payload: dict) -> list[str]:
    return ["df", "-h", "--", payload.get("path", "/")]


def storage_inodes(payload: dict) -> list[str]:
    return ["df", "-i", "--", payload.get("path", "/")]


def storage_lsblk(payload: dict) -> list[str]:
    return ["lsblk", "-o", "NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS,MODEL"]


def storage_mounts(payload: dict) -> list[str]:
    return ["findmnt", "-r"]


def storage_swap(payload: dict) -> list[str]:
    return ["swapon", "--show"]


def storage_du(payload: dict) -> list[str]:
    return ["du", "-sh", "--", payload["path"]]


def storage_stat(payload: dict) -> list[str]:
    return ["stat", "-f", "--", payload.get("path", "/")]
