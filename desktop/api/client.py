from typing import Literal, Any

import httpx

import logging

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


class NexoraClient:
    BASE_AGENT_URL = "agents/"

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token

        self.client = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {token}"},
            timeout=10,
        )

    def _request(
        self,
        method: MethodType = "GET",
        path: str = None,
        params: dict = None,
        json_data: dict = None,
        timeout: int = 10,
    ) -> Any:
        method_name = method.lower()

        try:
            request_func = getattr(self.client, method_name)

            kwargs = {"url": path, "params": params, "timeout": timeout}

            if method_name in ("post", "put", "patch") and json_data is not None:
                kwargs["json"] = json_data

            response = request_func(**kwargs)

            response.raise_for_status()

            return response.json() if response.content else {}

        except httpx.HTTPStatusError as e:
            logging.error(f"Server/client error [Status {e.response.status_code}]: {e}")
            return None

        except httpx.RequestError as e:
            logging.error(
                f"Network error while executing the request {e.request.url}: {e}"
            )
            return None

    def close(self):
        self.client.close()

    def get_agents_list(self) -> list[dict]:
        return self._request("get", self.BASE_AGENT_URL)

    def get_detail_agent(self, agent_id: int) -> dict:
        return self._request("get", f"{self.BASE_AGENT_URL}{agent_id}/")

    def get_agent_metrics(
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

        return self._request(
            method="get",
            path=metric_url,
            params=compiled_params,
        )

    def get_agent_commands(self, agent_id: int, count: int | str) -> list[dict]:
        return self._request(
            "get", f"{self.BASE_AGENT_URL}{agent_id}/commands/", {"count": count}
        )

    def create_agent_command(self, agent_id: int, command_type: str) -> dict | None:
        return self._request(
            method="post",
            path=f"{self.BASE_AGENT_URL}{agent_id}/commands/",
            json_data={"command_type": command_type},
        )
