from httpx import Client, HTTPError
import logging


class NexoraClient:
    BASE_AGENT_URL = "agents/"

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": self.token}

    def _get(
        self, path: str, params: dict = None, timeout: int = 10
    ) -> list[dict] | dict | None:
        with Client(
            base_url=self.base_url, headers=self.headers, timeout=timeout
        ) as client:
            try:
                response = client.get(url=path, params=params)

                response.raise_for_status()

                return response.json()

            except HTTPError as e:
                logging.error(f"HTTP Error during GET {path}: {e}")
                raise e

            except Exception as e:
                logging.error(f"Unexpected error during GET {path}: {e}")
                raise e

    def get_agents_list(self) -> list[dict]:
        return self._get(f"{self.BASE_AGENT_URL}")

    def get_detail_agent(self, agent_id: int) -> dict:
        return self._get(f"{self.BASE_AGENT_URL}{agent_id}/")

    def get_agent_metrics(
        self, agent_id: int, hours: int, metric_type: str, query_params: dict = {}
    ) -> dict:
        BASE_AGENT_METRIC_URL = f"{self.BASE_AGENT_URL}{agent_id}/metrics/"

        metric_types = {
            "resources": f"{BASE_AGENT_METRIC_URL}resources/",
            "thermals": f"{BASE_AGENT_METRIC_URL}thermals/",
            "network": f"{BASE_AGENT_METRIC_URL}network/",
            "storage": f"{BASE_AGENT_METRIC_URL}storage/",
        }

        metric_url = metric_types[metric_type]

        query_params.update({"hours": hours})

        return self._get(
            metric_url,
            query_params,
        )

    def get_agent_commands(self, agent_id: int, count: int | str) -> list[dict]:
        return self._get(f"{self.BASE_AGENT_URL}{agent_id}/commands/", {"count": count})
