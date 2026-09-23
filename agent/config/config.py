from dataclasses import dataclass

from decouple import config


@dataclass(frozen=True)
class Settings:
    api_url: str
    agent_id: int
    token: str
    heartbeat_interval: int = 5
    command_interval: int = 2

    def __post_init__(self):
        if not self.token or not self.token.strip():
            raise ValueError("NEXORA_TOKEN cannot be empty")


def load_settings() -> Settings:
    return Settings(
        api_url=config("NEXORA_API_URL"),
        agent_id=config("NEXORA_AGENT_ID", cast=int),
        token=config("NEXORA_TOKEN").strip(),
        heartbeat_interval=config("NEXORA_HEARTBEAT_INTERVAL", default=5, cast=int),
        command_interval=config("NEXORA_COMMAND_INTERVAL", default=2, cast=int),
    )
