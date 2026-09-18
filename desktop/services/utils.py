from typing import Literal

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
) -> str:
    """Convert bytes into a formatted higher-order unit string.

    Args:
        value: Raw byte count to convert. Must be non-negative.
        unit: Target storage unit (case-insensitive).
        precision: Number of decimal places to round. Must be non-negative.
        rate: Append rate suffix '/s' if True.

    Returns:
        Formatted string containing the converted value and unit.

    Raises:
        TypeError: If value is not numeric, or precision/rate have invalid types.
        ValueError: If value or precision is negative, or unit is invalid.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"value must be int or float, got {type(value).__name__}")

    if not isinstance(precision, int) or isinstance(precision, bool):
        raise TypeError(f"precision must be int, got {type(precision).__name__}")

    if not isinstance(rate, bool):
        raise TypeError(f"rate must be bool, got {type(rate).__name__}")

    if value < 0:
        raise ValueError(f"value must be non-negative, got {value}")

    if precision < 0:
        raise ValueError(f"precision must be non-negative, got {precision}")

    unit_key = unit.lower()

    if unit_key not in UNIT_MAP:
        valid_units = ", ".join(UNIT_MAP.keys()).upper()

        raise ValueError(f"Unsupported unit '{unit}'. Valid options: {valid_units}")

    factor = UNIT_MAP[unit_key]
    converted = value / (1024**factor)
    rate_suffix = "/s" if rate else ""

    return f"{converted:.{precision}f} {unit_key.upper()}{rate_suffix}"
