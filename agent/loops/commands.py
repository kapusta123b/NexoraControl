import asyncio

from commands.parser import command_parser
from config.config import COMMAND_INTERVAL
from api.client import BasicClient


async def get_command_loop():
    client = BasicClient()

    while True:

        response = await client.get_pengind_commands()

        await command_parser(response)

        await asyncio.sleep(COMMAND_INTERVAL)
