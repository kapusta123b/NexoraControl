import asyncio

from services.utils import get_system_hostname
from api.client import BasicClient

from loops.commands import get_command_loop
from loops.heartbeat import heartbeat_loop

from config import config


async def tune_config():
    if config.AGENT_ID == 0 or not config.TOKEN:
        print("--- Configuration for Agent ---")

        name = input("Enter name for your agent: ")
        hostname = get_system_hostname()

        response, status_code = await BasicClient().create_agent({"name": name, "hostname": hostname})
        
        if status_code == 201:
            new_agent_id = response.get("id")
            new_token = response.get("token")

            with open("agent/config/config.py", "w", encoding="utf-8") as f:
                f.write(f'API_URL = "{config.API_URL}"\n')
                f.write(f"AGENT_ID = {new_agent_id}\n")
                f.write(f'TOKEN = "{new_token}"\n')
                f.write(f"HEARTBEAT_INTERVAL = {config.HEARTBEAT_INTERVAL}\n")
                f.write(f"COMMAND_INTERVAL = {config.COMMAND_INTERVAL}\n")

        else:
            print('Error: API url not correct')

async def main():
    
    await asyncio.gather(
        heartbeat_loop(),
        get_command_loop(),
    )


if __name__ == "__main__":
    asyncio.run(tune_config())
    asyncio.run(main())