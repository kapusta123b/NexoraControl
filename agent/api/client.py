import logging
from typing import Any, Literal

import httpx

from config.config import Settings, load_settings

MethodType = Literal[
    "get",
    "post",
    "put",
    "patch",
    "head",
    "options",
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "HEAD",
    "OPTIONS",
]


class BasicClient:
    BASE_AGENT_URL = "agents/"

    def __init__(self, settings: Settings | None = None, base_url: str | None = None):
        self.settings = settings or load_settings()

        token_header = (
            self.settings.token
            if self.settings.token.startswith("Bearer ")
            else f"Bearer {self.settings.token}"
        )

        self.client = httpx.AsyncClient(
            base_url=base_url or self.settings.api_url,
            timeout=15.0,
            headers={
                "Authorization": token_header,
                "Content-Type": "application/json",
            },
            follow_redirects=True,
        )

    async def _request(
        self,
        method: MethodType = "GET",
        path: str = None,
        params: dict = None,
        json_data: dict = None,
        timeout: int = 10,
        return_status: bool = False,
    ) -> Any:
        method_name = method.lower()

        try:
            request_func = getattr(self.client, method_name)

            kwargs = {"url": path, "params": params, "timeout": timeout}

            if method_name in ("post", "put", "patch") and json_data is not None:
                kwargs["json"] = json_data

            response = await request_func(**kwargs)
            response.raise_for_status()

            validate = response.json() if response.content else {}

            if return_status:
                return validate, response.status_code

            return validate

        except AttributeError as e:
            logging.exception(f"Invalid method name: {e}")
            return (None, 0) if return_status else None

        except httpx.HTTPStatusError as e:
            logging.error(f"Server/client error [Status {e.response.status_code}]: {e}")
            return (None, e.response.status_code) if return_status else None

        except httpx.RequestError as e:
            logging.error(
                f"Network error while executing the request {e.request.url}: {e}"
            )
            return (None, 0) if return_status else None

    async def close(self):
        await self.client.close()

    async def create_agent(self, data: dict) -> tuple[dict | None, int]:
        response, status = await self._request(
            "post", f"{self.BASE_AGENT_URL}", json_data=data, return_status=True
        )
        return response, status

    async def send_heartbeat(self, heartbeat: dict) -> dict | None:
        return await self._request(
            "post",
            f"{self.BASE_AGENT_URL}{self.settings.agent_id}/heartbeat/",
            json_data=heartbeat,
        )

    async def get_pending_commands(self) -> dict | None:
        return await self._request(
            "get",
            f"{self.BASE_AGENT_URL}{self.settings.agent_id}/commands/pending",
        )

    async def send_commands(self, commands: list[dict]) -> dict | None:
        return await self._request(
            "patch",
            f"{self.BASE_AGENT_URL}{self.settings.agent_id}/commands/results/",
            json_data=commands,
        )
