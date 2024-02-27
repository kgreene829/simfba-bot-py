import discord
from discord.ext import commands
from discord import app_commands
from helper import cbb_stream_builder
import settings

channel_id = settings.ESPN2_STREAM_CHANNEL

class ESPN_2_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="espn_2_a", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn2', input, 'a')

    @app_commands.command(name="espn_2_b", description="The timeslot you'd like to stream")
    async def b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn2', input, 'b')

    @app_commands.command(name="espn_2_c", description="The timeslot you'd like to stream")
    async def c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn2', input, 'c')

    @app_commands.command(name="espn_2_d", description="The timeslot you'd like to stream")
    async def d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA ESPN Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'espn2', input, 'd')

async def setup(client: commands.Bot):
    await client.add_cog(ESPN_2_Stream(client))