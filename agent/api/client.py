from httpx import AsyncClient

from config import config


class BasicClient:

    def __init__(self):
        self.client = AsyncClient(
            base_url=config.API_URL,
            timeout=25,
            headers={"Authorization": config.TOKEN, "Content-Type": "application/json"},
            http2=False,
            follow_redirects=True,
        )

    async def create_agent(self, data: dict) -> tuple[dict, int]:
        response = await self.client.post(f"agents/", json=data)

        status_code = response.status_code

        return response.json(), status_code

    async def send_heartbeat(self, heartbeat: dict) -> None:
        response = await self.client.post(
            f"agents/{config.AGENT_ID}/heartbeat/", json=heartbeat
        )
        response.raise_for_status()

    async def get_pengind_commands(self) -> dict:
        response = await self.client.get(f"agents/{config.AGENT_ID}/commands/pending", )
        response.raise_for_status()

        return response.json()

    async def send_commands(self, commands: list[dict]) -> None:
        response = await self.client.patch(
            f"agents/{config.AGENT_ID}/commands/results/", json=commands
        )
        response.raise_for_status()