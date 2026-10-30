from dataclasses import dataclass
from urllib.parse import urlsplit, urlunsplit

DEFAULT_API_BASE_URL = "http://127.0.0.1:8000/api/v1/"
ORGANIZATION_NAME = "NexoraControl"
APPLICATION_NAME = "Desktop"


@dataclass(frozen=True, slots=True)
class DesktopPreferences:
    api_base_url: str = DEFAULT_API_BASE_URL
    auto_refresh_enabled: bool = True
    refresh_interval_seconds: int = 10
    request_timeout_seconds: int = 15
    confirm_dangerous_commands: bool = True
    notify_failures: bool = True


def normalize_api_base_url(value: str) -> str:
    if not isinstance(value, str):
        raise ValueError("The API URL must be text.")

    raw = value.strip()
    if not raw:
        raise ValueError("Enter the backend API URL.")

    try:
        parsed = urlsplit(raw)
        _ = parsed.port
    except ValueError as exc:
        raise ValueError(f"Invalid API URL: {exc}") from exc

    if parsed.scheme.lower() not in {"http", "https"}:
        raise ValueError("The API URL must start with http:// or https://.")

    if not parsed.hostname or not parsed.netloc:
        raise ValueError("The API URL must include a hostname.")

    if parsed.username or parsed.password:
        raise ValueError("Do not put credentials inside the API URL.")

    if parsed.query or parsed.fragment:
        raise ValueError(
            "The API base URL must not contain a query string or fragment."
        )

    path = parsed.path.rstrip("/")

    if path != "/api/v1" and not path.endswith("/api/v1"):
        raise ValueError("Include the API prefix, for example /api/v1/.")

    return urlunsplit((parsed.scheme.lower(), parsed.netloc, f"{path}/", "", ""))
