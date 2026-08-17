def system_cpu_info_output(result: dict, payload: dict) -> dict:
    trimmed_lines = []

    for line in result.get("output").splitlines():
        trimmed_lines.append(line)
        if "BogoMIPS" in line:
            break

    output_text = "\n".join(trimmed_lines)
    result["output"] = output_text

    return result


def system_processes_output(result: dict, payload: dict) -> dict:
    displayed_lines = payload["lines"]
    output = result.get("output")

    lines = output.split("\n")
    limited_output = "\n".join(lines[: displayed_lines + 1])

    result["output"] = limited_output
    return result
