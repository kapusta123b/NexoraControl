from typing import Literal

from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

UnitType = Literal["kb", "mb", "gb", "tb", "pb", "KB", "MB", "GB", "TB", "PB"]

UNIT_MAP: dict[str, int] = {
    "kb": 1,
    "mb": 2,
    "gb": 3,
    "tb": 4,
    "pb": 5,
}


def byte_converter(
    value: int | float,
    unit: UnitType = "mb",
    precision: int = 2,
    rate: bool = False,
    as_float: bool = False,
) -> str | float:
    """Convert bytes into a formatted higher-order unit string.

    Args:
        value: Raw byte count to convert. Must be non-negative.
        unit: Target storage unit (case-insensitive).
        precision: Number of decimal places to round. Must be non-negative.
        rate: Append rate suffix '/s' if True.
        as_float: result in bytes consists solely of integers, without string data.

    Returns:
        Formatted string containing the converted value and the unit of measurement, or an integer number of bytes.

    Raises:
        TypeError: If value is not numeric, or precision/rate have invalid types.
        ValueError: If value or precision is negative, or unit is invalid.
    """

    if not isinstance(value, (int, float)):
        raise TypeError(f"value must be int or float, got {type(value).__name__}")

    if not isinstance(precision, int):
        raise TypeError(f"precision must be int, got {type(precision).__name__}")

    if not isinstance(rate, bool):
        raise TypeError(f"rate argument must be bool, got {type(rate).__name__}")

    if not isinstance(as_float, bool):
        raise TypeError(f"as_float argument must be bool, got {type(rate).__name__}")

    if value < 0:
        raise ValueError(f"value must be non-negative, got {value}")

    if precision < 0:
        raise ValueError(f"precision must be non-negative, got {precision}")

    unit_key = unit.lower()

    if unit_key not in UNIT_MAP:
        valid_units = ", ".join(UNIT_MAP.keys()).upper()

        raise ValueError(f"Unsupported unit '{unit}'. Valid options: {valid_units}")

    factor = UNIT_MAP[unit_key]
    # division by a value with a data unit multiplier
    converted = value / (1024**factor)

    converted_with_precision = round(converted, precision)

    if as_float:
        # if the as_float parametr, return the converted float value without suffixes
        return converted_with_precision

    rate_suffix = "/s" if rate else ""

    return f"{converted_with_precision} {unit_key.upper()}{rate_suffix}"


def calculate_bytes_per_second(
    raw_bytes: list[int],
    timestamps: list[int],
    unit: UnitType = "mb",
) -> list[float]:
    """Calculate list of bytes into a speed by data unit.

    Args:
        raw_bytes (list[int]): a list of raw bytes to convert; the length must be greater than or equal to 2, and the list must contain integers.
        timestamps (list[int]): list of UNIX time, must be have the same lenght of raw_bytes.
        unit (UnitType): target data unit (case-insensitive).

    Returns:
        list[float]: list of speed values ​​(in bytes)
    """
    speed_in_bytes = []

    if raw_bytes and len(raw_bytes) == len(timestamps):
        for i in range(
            1, len(raw_bytes)
        ):  # time and bytes difference between two timestamps for calculating the correct speed in seconds
            delta_raw_bytes = raw_bytes[i] - raw_bytes[i - 1]
            delta_time = timestamps[i] - timestamps[i - 1]

            if delta_time > 0 and delta_raw_bytes >= 0:
                bytes_per_second = delta_raw_bytes / delta_time
            else:
                bytes_per_second = 0

            converted_speed = byte_converter(
                bytes_per_second,
                unit=unit,
                precision=4,
                as_float=True,
            )
            speed_in_bytes.append(converted_speed)

    return speed_in_bytes


def calculate_metric_rate(
    current_data: dict, last_data: dict, key: str, delta_time: float
) -> float:

    if delta_time <= 0:
        return 0.0

    delta_value = current_data.get(key, 0) - last_data.get(key, 0)

    return max(0.0, delta_value / delta_time)
