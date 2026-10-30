from typing import Any, Literal
import httpx

MethodType = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]


class NexoraAgentClient:
    def __init__(self, request_func) -> None:
        self._request = request_func
        self.path = "agents/"

    async def get_list(self) -> list[dict]:
        return await self._request("GET", self.path)

    async def get_detail(self, agent_id: int) -> dict:
        return await self._request("GET", f"{self.path}{agent_id}/")


class NexoraCommandClient:
    def __init__(self, request_func) -> None:
        self._request = request_func
        self.path = "agents/"

    async def get_commands(self, agent_id: int, params: dict = {}) -> list[dict]:
        return await self._request(
            "GET", f"{self.path}{agent_id}/commands/", params=params
        )

    async def create_command(
        self, agent_id: int, command_type: str, payload: dict = {}
    ) -> dict:
        return await self._request(
            "POST",
            f"{self.path}{agent_id}/commands/",
            json_data={
                "command_type": command_type,
                "payload": payload,
            },
        )


class NexoraMetricClient:
    def __init__(self, request_func) -> None:
        self._request = request_func
        self.path = "agents/"

    async def get_agent_metrics(
        self,
        agent_id: int,
        hours: int,
        metric_type: Literal["resource", "thermal", "network", "storage"],
        query_params: dict | None = None,
    ) -> dict:
        base_metric_url = f"{self.path}{agent_id}/metrics/"

        metric_types = {
            "resource": f"{base_metric_url}resource/",
            "thermal": f"{base_metric_url}thermal/",
            "network": f"{base_metric_url}network/",
            "storage": f"{base_metric_url}storage/",
        }

        metric_url = metric_types.get(metric_type)
        if not metric_url:
            raise ValueError(
                f"Incorrect metric type: {metric_type}. Available: {list(metric_types.keys())}"
            )

        compiled_params = dict(query_params) if query_params else {}
        compiled_params.update({"hours": hours})

        return await self._request(
            method="GET",
            path=metric_url,
            params=compiled_params,
        )


class NexoraHardwareInfoClient:
    def __init__(self, request_func) -> None:
        self._request = request_func
        self.path = "agents/"

    async def get_system_information(
        self, agent_id
    ) -> dict[str, dict | list[dict] | str]:

        return await self._request(
            method="GET", path=f"{self.path}{agent_id}/system-info/"
        )


class NexoraClient:
    def __init__(
        self, base_url: str, token: str, timeout_seconds: float = 15.0
    ) -> None:
        self.base_url = base_url
        self.token = token
        self.timeout_seconds = float(timeout_seconds)
        # Desktop preferences shared by command controllers and pollers.
        self.confirm_dangerous_commands = True
        self.notify_failures = True

        self.agents = NexoraAgentClient(self._request)
        self.commands = NexoraCommandClient(self._request)
        self.metrics = NexoraMetricClient(self._request)
        self.hardware = NexoraHardwareInfoClient(self._request)

    async def _request(
        self, method: MethodType, path: str, params: dict = None, json_data: dict = None
    ) -> Any:
        async with httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            timeout=self.timeout_seconds,
        ) as client:
            kwargs = {"params": params}
            if method in ("POST", "PUT", "PATCH") and json_data is not None:
                kwargs["json"] = json_data

            response = await client.request(method, path, **kwargs)
            response.raise_for_status()
            return response.json() if response.content else {}

    async def __aenter__(self):
        return self
