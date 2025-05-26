import discord
from discord.ext import commands
from discord import app_commands
from helper import hockey_stream_builder
import settings
import asyncio


channel_id = settings.RINK_STREAM_CHANNEL

class Hockey_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="the_classic", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("For those here who are about to witness this, I want to thank you for your being a part of this community and an active participant in our sports sims.")
        await asyncio.sleep(4)
        await chan.send("What you are about to see is something that's been a secret for a couple of months...")
        await asyncio.sleep(4)
        await chan.send("This is a passion project, and a love letter to a sport that deserves more recognition.")
        await hockey_stream_builder.stream_hockey_game(chan, '', input, 'a')


async def setup(client: commands.Bot):
    await client.add_cog(Hockey_Stream(client))