from httpx import Client

import asyncio


class NexoraClient:

    def __init__(self, base_url, token):
        self.client = Client(
            base_url=base_url,
            headers={"Authorization": token},
            timeout=10,
        )

    def get_agents(self):

        response = self.client.get("agents/")

        response.raise_for_status()

        return response.json()


# client = NexoraClient(
#     "http://127.0.0.1:8000/api/v1/", "30287dfd-d1ae-4efb-aa89-e26cf089bcb4"
# )


# agents = client.get_agents()


# print(agents)
