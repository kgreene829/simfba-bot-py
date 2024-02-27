import discord
from discord.ext import commands
from discord import app_commands
from helper import nba_stream_builder
import settings

channel_id = settings.TNT_STREAM_CHANNEL

class TNT_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="tnt_a", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', input, 'a')

    @app_commands.command(name="tnt_b", description="The timeslot you'd like to stream")
    async def b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', input, 'b')

    @app_commands.command(name="tnt_c", description="The timeslot you'd like to stream")
    async def c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', input, 'c')

    @app_commands.command(name="tnt_d", description="The timeslot you'd like to stream")
    async def d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA TNT Games...")
        await nba_stream_builder.stream_game(chan, 'tnt', input, 'd')

async def setup(client: commands.Bot):
    await client.add_cog(TNT_Stream(client))