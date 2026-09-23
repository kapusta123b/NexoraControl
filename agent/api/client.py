from httpx import AsyncClient

from config.config import Settings, load_settings


import httpx
from httpx import AsyncClient


class BasicClient:

    def __init__(self, settings: Settings | None = None, base_url: str | None = None):
        self.settings = settings or load_settings()

        token_header = (
            self.settings.token
            if self.settings.token.startswith("Bearer ")
            else f"Bearer {self.settings.token}"
        )

        self.client = AsyncClient(
            base_url=base_url or self.settings.api_url,
            timeout=25.0,
            headers={
                "Authorization": token_header,
                "Content-Type": "application/json",
            },
            follow_redirects=True,
        )

    async def create_agent(self, data: dict) -> tuple[dict, int]:
        response = await self.client.post("agents/", json=data)

        status_code = response.status_code

        return response.json(), status_code

    async def send_heartbeat(self, heartbeat: dict) -> None:
        response = await self.client.post(
            f"agents/{self.settings.agent_id}/heartbeat/", json=heartbeat
        )
        response.raise_for_status()

    async def get_pengind_commands(self) -> dict:
        response = await self.client.get(
            f"agents/{self.settings.agent_id}/commands/pending",
        )
        response.raise_for_status()

        return response.json()

    async def send_commands(self, commands: list[dict]) -> None:
        response = await self.client.patch(
            f"agents/{self.settings.agent_id}/commands/results/", json=commands
        )
        response.raise_for_status()
