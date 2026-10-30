from __future__ import annotations

from urllib.parse import urljoin

import httpx
from PySide6.QtCore import QObject, Signal, Slot


class ConnectionTestWorker(QObject):
    result = Signal(str, str, str)
    finished = Signal()

    def __init__(self, base_url: str, timeout_seconds: int) -> None:
        super().__init__()
        self.base_url = base_url
        self.timeout_seconds = timeout_seconds

    @Slot()
    def run(self) -> None:
        headers = {"Accept": "application/json"}

        try:
            endpoint = urljoin(self.base_url, "agents/")
            with httpx.Client(
                timeout=float(self.timeout_seconds), follow_redirects=True
            ) as http:
                response = http.get(endpoint, headers=headers)

            status_code = response.status_code
            if 200 <= status_code < 400:
                self.result.emit(
                    "connected",
                    f"CONNECTED · HTTP {status_code}",
                    f"The API endpoint responded successfully (HTTP {status_code}).",
                )
            elif status_code in (401, 403):
                self.result.emit(
                    "auth",
                    f"REACHABLE · HTTP {status_code}",
                    "The server is reachable, but this endpoint requires authentication or permissions. This test does not send a token.",
                )
            elif status_code == 404:
                self.result.emit(
                    "warning",
                    "ENDPOINT NOT FOUND",
                    "The server responded, but /agents/ was not found. Check that the base URL includes /api/v1/.",
                )
            elif status_code >= 500:
                self.result.emit(
                    "error",
                    f"SERVER ERROR · HTTP {status_code}",
                    "The backend responded but returned a server error. Check backend logs.",
                )
            else:
                self.result.emit(
                    "warning",
                    f"HTTP {status_code}",
                    f"The server responded with HTTP {status_code}.",
                )
        except httpx.ConnectTimeout:
            self.result.emit(
                "error",
                "CONNECTION TIMEOUT",
                "The connection timed out before the server responded.",
            )
        except httpx.ConnectError as exc:
            self.result.emit(
                "error", "CONNECTION FAILED", f"Could not connect to the backend: {exc}"
            )
        except httpx.TimeoutException:
            self.result.emit(
                "error",
                "REQUEST TIMEOUT",
                "The backend did not respond before the timeout.",
            )
        except httpx.HTTPError as exc:
            self.result.emit("error", "HTTP ERROR", str(exc))
        except Exception as exc:
            self.result.emit("error", "TEST FAILED", str(exc))
        finally:
            self.finished.emit()
