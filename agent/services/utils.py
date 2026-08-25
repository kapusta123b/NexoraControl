import subprocess
import platform
import os
import urllib.request

def get_system_hostname() -> str:
    name = subprocess.run("hostname", capture_output=True, text=True).stdout.strip()

    return name


def get_public_ip_native() -> str:
    try:
        with urllib.request.urlopen('https://ifconfig.me', timeout=5) as response:
            return response.read().decode('utf-8').strip()
    except Exception:
        return "Unknown"
    
def get_os_info() -> str:
    system = platform.system()
    
    if system == "Linux":
        if hasattr(platform, "freedesktop_os_release"):
            try:
                info = platform.freedesktop_os_release()
                name = info.get("NAME", "Linux")
                version = info.get("VERSION_ID", "")
                return f"{name} {version}".strip()
            except OSError:
                pass
        return f"Linux {platform.release()}"
        
    elif system == "Windows":
        return f"Windows {platform.release()}"
        
    elif system == "Darwin":
        return f"macOS {platform.mac_ver()[0]}"
        
    return system


