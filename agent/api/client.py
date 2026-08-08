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

    async def send_heartbeat(self, params: dict) -> int:
        response = await self.client.post(f"agents/{AGENT_ID}/heartbeat/", json=params)
        status_code = response.status_code

        return status_code
