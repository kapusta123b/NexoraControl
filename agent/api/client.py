from httpx import AsyncClient

from config.config import AGENT_ID, API_URL, TOKEN


class BasicClient:

    def __init__(self):
        self.client = AsyncClient(
            base_url=API_URL,
            timeout=25,
            headers={"Authorization": TOKEN, "Content-Type": "application/json"},
            http2=False,
            follow_redirects=True,
        )

    async def send_heartbeat(self, heartbeat: dict) -> int:
        response = await self.client.post(f"agents/{AGENT_ID}/heartbeat/", json=heartbeat)
        status_code = response.status_code

        return status_code

    async def get_commands(self, params: dict) -> dict | int:
        response = await self.client.get(f"agents/{AGENT_ID}/commands/", params=params)
        status_code = response.status_code

        return response.json()[0], status_code

    async def send_commands(self, commands: list[dict]) -> int:
        response = await self.client.patch(
            f"agents/{AGENT_ID}/commands/results/", json=commands
        )
        status_code = response.status_code

        return status_code
