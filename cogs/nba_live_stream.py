import discord
from discord.ext import commands
from discord import app_commands
from helper import nba_stream_builder
import settings

channel_id = settings.NBA_LIVE_STREAM_CHANNEL

class NBA_Live_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="nbatv_a", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', input, 'a')

    @app_commands.command(name="nbatv_b", description="The timeslot you'd like to stream")
    async def b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', input, 'b')

    @app_commands.command(name="nbatv_c", description="The timeslot you'd like to stream")
    async def c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', input, 'c')

    @app_commands.command(name="nbatv_d", description="The timeslot you'd like to stream")
    async def d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA NBATV Games...")
        await nba_stream_builder.stream_game(chan, 'nbatv', input, 'd')

async def setup(client: commands.Bot):
    await client.add_cog(NBA_Live_Stream(client))