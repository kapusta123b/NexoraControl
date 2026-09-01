from httpx import Client


class NexoraClient:

    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.token = token

        self.client = Client(
            base_url=self.base_url,
            headers={"Authorization": self.token},
            timeout=10,
        )

    def get_agents(self) -> list[dict]:

        response = self.client.get("agents/")

        response.raise_for_status()

        return response.json()

    def get_agent_resource_metrics(self, agent_id, hours) -> dict:

        response = self.client.get(
            f"agents/{agent_id}/metrics/resources/",
            params={"hours": hours},
        )

        response.raise_for_status()

        return response.json()
