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
        self, agent_id: int, hours: int, metric_type: str, partial: bool
    ) -> dict:
        BASE_AGENT_METRIC_URL = f"{self.BASE_AGENT_URL}{agent_id}/metrics/"
        url_for_last_metric = "latest" if partial else "history"

        metric_types = {
            "resources": f"{BASE_AGENT_METRIC_URL}resources/{url_for_last_metric}/",
            "thermals": f"{BASE_AGENT_METRIC_URL}thermals/{url_for_last_metric}/",
            "network": f"{BASE_AGENT_METRIC_URL}network/{url_for_last_metric}/",
            "storage": f"{BASE_AGENT_METRIC_URL}storage/{url_for_last_metric}/",
        }

        metric_url = metric_types[metric_type]

        return self._get(
            metric_url,
            {"hours": hours},
        )

    def get_agent_commands(self, agent_id: int, count: int | str) -> list[dict]:
        return self._get(f"{self.BASE_AGENT_URL}{agent_id}/commands/", {"count": count})
