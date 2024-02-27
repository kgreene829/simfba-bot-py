import discord
from discord.ext import commands
from discord import app_commands
from helper import cbb_stream_builder
import settings

channel_id = settings.TBS_STREAM_CHANNEL

class TBS_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="tbs_a", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', input, 'a')

    @app_commands.command(name="tbs_b", description="The timeslot you'd like to stream")
    async def b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', input, 'b')

    @app_commands.command(name="tbs_c", description="The timeslot you'd like to stream")
    async def c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', input, 'c')

    @app_commands.command(name="tbs_d", description="The timeslot you'd like to stream")
    async def d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA TBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'tbs', input, 'd')

async def setup(client: commands.Bot):
    await client.add_cog(TBS_Stream(client))