import subprocess


def system_uptime(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["uptime", "-p"], capture_output=True, text=True, check=True
        )
        return {"status": "SUCCESS", "output": result.stdout.strip()}

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() or f"The command finished with code {e.returncode}"
        return {"status": "FAILED", "output": error_msg}

    except Exception as e:
        return {"status": "FAILED", "output": str(e)}


def system_os_info(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["cat", "/etc/os-release"], capture_output=True, text=True, check=True
        )
        return {"status": "SUCCESS", "output": result.stdout}

    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}


def system_cpu_info(payload: dict) -> dict:
    try:
        result = subprocess.run(["lscpu"], check=True, text=True, capture_output=True)

        trimmed_lines = []
        for line in result.stdout.splitlines():
            trimmed_lines.append(line)
            if "BogoMIPS" in line:
                break

        output_text = "\n".join(trimmed_lines)

        return {"status": "SUCCESS", "output": output_text}

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}


def system_ram_info(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["free", "-h"],
            check=True,
            text=True,
            capture_output=True,
        )
        return {"status": "SUCCESS", "output": result.stdout}

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}


def system_disk_info(payload: dict) -> dict:
    try:
        result = subprocess.run(
            ["lsblk"],
            check=True,
            text=True,
            capture_output=True,
        )
        return {"status": "SUCCESS", "output": result.stdout}

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr if hasattr(e, "stderr") else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}
    
def system_processes(payload: dict) -> dict:
    try:
        head = payload.get("head", 6)
        
        result = subprocess.run(
            ["ps", "-eo", "pid,ppid,%cpu,%mem,comm", "--sort=-%cpu"],
            check=True,
            text=True,
            capture_output=True,
        )
        
        lines = result.stdout.strip().split("\n")
        limited_output = "\n".join(lines[:head + 1])
        
        return {"status": "SUCCESS", "output": limited_output}
    
    except Exception as e:
        error_msg = e.stderr if isinstance(e, subprocess.CalledProcessError) else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}
    
def system_reboot(payload: dict) -> dict:
    try:
        subprocess.run(
            ["systemctl", "reboot"],
            check=True,
            text=True,
            capture_output=True,
        )
        
    except Exception as e:
        error_msg = e.stderr if isinstance(e, subprocess.CalledProcessError) else str(e)
        return {"status": "FAILED", "output": error_msg.strip()}