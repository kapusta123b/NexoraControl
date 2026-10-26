import json
import os
import platform
import re
import subprocess
from pathlib import Path

import psutil

UNKNOWN = "Not Available"
SYSFS = Path("/sys")


def _text(path: Path) -> str:
    try:
        value = path.read_text(encoding="utf-8", errors="replace").strip()
        if value and value.lower() not in ("none", "unknown", "to be filled by o.e.m."):
            return value
    except OSError:
        pass
    return UNKNOWN


def _size(value: object) -> str:
    """Convert a byte count to a human-readable IEC capacity."""
    try:
        size = int(value)
        if size < 0:
            raise ValueError
    except (TypeError, ValueError, OverflowError):
        return UNKNOWN
    for unit in ("B", "KiB", "MiB", "GiB", "TiB", "PiB"):
        if size < 1024 or unit == "PiB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return UNKNOWN


class ProductionParser:
    """Read Linux inventory using lscpu, lspci, lsblk, sysfs and psutil."""

    @staticmethod
    def run_cmd(args: list[str], timeout: int = 4) -> str:
        try:
            result = subprocess.run(
                args,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                check=False,
                env={**os.environ, "LC_ALL": "C"},
            )
            return result.stdout.strip() if result.returncode == 0 else ""
        except (OSError, subprocess.TimeoutExpired):
            return ""

    @classmethod
    def get_cpu(cls) -> dict:
        try:
            entries = json.loads(cls.run_cmd(["lscpu", "-J"]))["lscpu"]
            fields = {
                item["field"].rstrip(":").strip(): item.get("data") for item in entries
            }
        except (ValueError, TypeError, KeyError):
            fields = {}

        freq = UNKNOWN
        try:
            speed = psutil.cpu_freq()
            if speed and speed.min and speed.max and speed.min <= speed.max:
                freq = f"{speed.min / 1000:g}-{speed.max / 1000:g} GHz"

        except (OSError, RuntimeError, ValueError):

            pass

        l1 = [fields.get(key) for key in ("L1d cache", "L1i cache")]

        physical = psutil.cpu_count(logical=False)

        logical = psutil.cpu_count(logical=True)

        return {
            "model": fields.get("Model name") or platform.processor() or UNKNOWN,
            "architecture": fields.get("Architecture") or platform.machine() or UNKNOWN,
            "physical_cores": str(physical) if physical else UNKNOWN,
            "logical_threads": str(logical) if logical else UNKNOWN,
            "frequency": freq,
            "l1_cache": " + ".join(x for x in l1 if x) or UNKNOWN,
            "l2_cache": fields.get("L2 cache") or UNKNOWN,
            "l3_cache": fields.get("L3 cache") or UNKNOWN,
        }

    @classmethod
    def get_gpus(cls) -> list[dict]:
        nvidia = {}

        for row in cls.run_cmd(
            [
                "nvidia-smi",
                "--query-gpu=pci.bus_id,memory.total,driver_version",
                "--format=csv,noheader,nounits",
            ]
        ).splitlines():
            parts = [part.strip() for part in row.split(",")]

            if len(parts) == 3:
                bus, memory, version = parts

                bus = bus.lower()
                # nvidia-smi uses 00000000:01:00.0; lspci uses 0000:01:00.0.
                if re.fullmatch(r"[\da-f]{8}:[\da-f]{2}:[\da-f]{2}\.[0-7]", bus):
                    bus = bus[-12:]

                elif re.fullmatch(r"[\da-f]{2}:[\da-f]{2}\.[0-7]", bus):
                    bus = "0000:" + bus
                try:
                    vram = _size(int(float(memory)) * 1024 * 1024)

                except (ValueError, OverflowError):
                    vram = UNKNOWN

                nvidia[bus] = (vram, version or UNKNOWN)

        cards = []

        for row in cls.run_cmd(["lspci", "-D", "-nn"]).splitlines():
            match = re.match(r"^(\S+)\s+(.+?):\s+(.+)$", row)

            if not match:
                continue

            bus, category, model = match.groups()

            if not any(
                x in category.lower()
                for x in ("vga compatible", "3d controller", "display controller")
            ):
                continue

            driver_path = SYSFS / "bus/pci/devices" / bus / "driver"

            try:
                driver = driver_path.resolve(strict=True).name

            except OSError:
                driver = UNKNOWN

            vram, nvidia_version = nvidia.get(bus.lower(), (UNKNOWN, UNKNOWN))

            if nvidia_version != UNKNOWN:
                driver = (
                    f"NVIDIA {nvidia_version} ({driver})"
                    if driver != UNKNOWN
                    else f"NVIDIA {nvidia_version}"
                )

            cards.append(
                {
                    "device": f"GPU {len(cards)}",
                    "model": model,
                    "vram": vram,
                    "driver_version": driver,
                    "interface": f"PCI {bus}",
                }
            )

        return cards

    @staticmethod
    def get_ram_slots() -> list[dict]:
        return [
            {"slot": "System total", "capacity": _size(psutil.virtual_memory().total)}
        ]

    @staticmethod
    def get_motherboard_bios() -> dict:
        base = SYSFS / "class/dmi/id"
        return {
            "board_vendor": _text(base / "board_vendor"),
            "board_model": _text(base / "board_name"),
            "bios_vendor": _text(base / "bios_vendor"),
            "bios_version": _text(base / "bios_version"),
            "release_date": _text(base / "bios_date"),
        }

    @classmethod
    def get_storage(cls) -> list[dict]:
        try:
            rows = json.loads(
                cls.run_cmd(
                    [
                        "lsblk",
                        "-J",
                        "-b",
                        "-d",
                        "-o",
                        "NAME,TYPE,MODEL,SIZE,TRAN",
                    ]
                )
            ).get("blockdevices", [])
        except (ValueError, TypeError, AttributeError):
            return []
        result = []
        for disk in rows:
            if not isinstance(disk, dict) or disk.get("type") != "disk":
                continue
            name = disk.get("name")
            if not name:
                continue
            result.append(
                {
                    "device": f"/dev/{name}",
                    "model": disk.get("model") or UNKNOWN,
                    "capacity": _size(disk.get("size")),
                    "interface": (
                        (
                            disk.get("tran")
                            or ("nvme" if name.startswith("nvme") else UNKNOWN)
                        ).upper()
                        if (disk.get("tran") or name.startswith("nvme"))
                        else UNKNOWN
                    ),
                }
            )
        return result

    @classmethod
    def get_network(cls) -> list[dict]:
        adapters = []
        for name, state in sorted(psutil.net_if_stats().items()):
            device = SYSFS / "class/net" / name
            if name == "lo" or not (device / "device").exists():
                continue

            mac = _text(device / "address")
            pci_id = (device / "device").resolve().name
            model = UNKNOWN

            if re.fullmatch(
                r"[\da-fA-F]{4}:[\da-fA-F]{2}:[\da-fA-F]{2}\.[0-7]", pci_id
            ):
                match = cls.run_cmd(["lspci", "-s", pci_id, "-nn"])
                if ": " in match:
                    model = match.split(": ", 1)[1].splitlines()[0]

            adapters.append(
                {
                    "interface": name,
                    "model": model,
                    "mac_adresses": mac,
                    "link_type": (
                        "Wi-Fi"
                        if name.startswith("wl") or (device / "wireless").exists()
                        else "Ethernet"
                    ),
                    "status": "UP" if state.isup else "DOWN",
                }
            )
        return adapters

    @classmethod
    def collect(cls) -> dict:
        return {
            "cpu_info": cls.get_cpu(),
            "gpu_info": cls.get_gpus(),
            "memory_info": cls.get_ram_slots(),
            "motherboard_bios_info": cls.get_motherboard_bios(),
            "storage_info": cls.get_storage(),
            "network_info": cls.get_network(),
        }
