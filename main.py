import discord
import os
from discord.ext import commands
from discord import app_commands
from constants import *
import settings

class MyClient(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='/', intents=discord.Intents.default())
        self.intents.message_content = True
    async def setup_hook(self):
        list_dir = os.listdir('./cogs')
        for filename in list_dir:
                if filename.endswith('.py'):
                    await self.load_extension(f'cogs.{filename[:-3]}')
        
    async def on_ready(self):
        self.tree.copy_global_to(guild=settings.GUILDS_ID)
        synced = await self.tree.sync(guild=settings.GUILDS_ID)
        print(f'Logged on as {self.user}!')
        print("Slash CMDs Synced: " + str(len(synced)))

    async def on_error(self, event, *args, **kwargs):
        print(f"An error occurred in event {event}, args: {args}, kwargs: {kwargs}")

client = MyClient()

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

@client.tree.command()
async def test(interaction: discord.Interaction):
    """Sends the text into the current channel."""
    await interaction.response.send_message("HELLO THERE!")

client.run(settings.DISCORD_API_SECRET, root_logger=True)