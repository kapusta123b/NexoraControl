import asyncio

from commands.parser import command_parser

async def get_command_loop(client):

    while True:
        response = await client.get_pengind_commands()

        await command_parser(response)

        await asyncio.sleep(client.settings.command_interval)
