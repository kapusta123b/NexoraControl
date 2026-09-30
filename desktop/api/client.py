from typing import Any, Literal

import httpx

MethodType = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]


class NexoraClient:
    BASE_AGENT_URL = "agents/"

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    async def _request(
        self, method: MethodType, path: str, params: dict = None, json_data: dict = None
    ) -> Any:
        async with httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            timeout=10.0,
        ) as client:
            request_func = getattr(client, method.lower())
            kwargs = {"url": path, "params": params}
            if method in ("POST", "PUT", "PATCH") and json_data is not None:
                kwargs["json"] = json_data

            response = await request_func(**kwargs)
            response.raise_for_status()
            return response.json() if response.content else {}

    async def get_agents_list(self) -> list[dict]:
        return await self._request("GET", self.BASE_AGENT_URL)

    async def get_detail_agent(self, agent_id: int) -> dict:
        return await self._request("GET", f"{self.BASE_AGENT_URL}{agent_id}/")

    async def get_agent_commands(self, agent_id: int, count: int) -> list[dict]:
        return await self._request(
            "GET", f"{self.BASE_AGENT_URL}{agent_id}/commands/", params={"count": count}
        )

    async def create_agent_command(self, agent_id: int, command_type: str) -> dict:
        return await self._request(
            "POST",
            f"{self.BASE_AGENT_URL}{agent_id}/commands/",
            json_data={"command_type": command_type},
        )

    async def get_agent_metrics(
        self,
        agent_id: int,
        hours: int,
        metric_type: str,
        query_params: dict | None = None,
    ) -> dict:

        BASE_AGENT_METRIC_URL = f"{self.BASE_AGENT_URL}{agent_id}/metrics/"

        metric_types = {
            "resources": f"{BASE_AGENT_METRIC_URL}resources/",
            "thermals": f"{BASE_AGENT_METRIC_URL}thermals/",
            "network": f"{BASE_AGENT_METRIC_URL}network/",
            "storage": f"{BASE_AGENT_METRIC_URL}storage/",
        }

        metric_url = metric_types[metric_type]

        compiled_params = dict(query_params) if query_params else {}
        compiled_params.update({"hours": hours})

        return await self._request(
            method="get",
            path=metric_url,
            params=compiled_params,
        )
