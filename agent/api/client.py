from httpx import AsyncClient

from config.config import Settings

from config.config import load_settings


class BasicClient:

    def __init__(self, settings=None, base_url=None):
        self.settings = settings or load_settings()

        self.client = AsyncClient(
            base_url=base_url or self.settings.api_url,
            timeout=25,
            headers={
                "Authorization": self.settings.token,
                "Content-Type": "application/json",
            },
            follow_redirects=True,
        )

    async def create_agent(self, data: dict) -> tuple[dict, int]:
        response = await self.client.post(f"agents/", json=data)

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
