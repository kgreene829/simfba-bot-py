import discord
from discord.ext import commands
from discord import app_commands
from helper import cbb_stream_builder
import settings

channel_id = settings.CBB_STREAM_CHANNEL

class BBA_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cbb_a", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA CBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'cbs', input, 'a')

    @app_commands.command(name="cbb_b", description="The timeslot you'd like to stream")
    async def b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA CBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'cbs', input, 'b')

    @app_commands.command(name="cbb_c", description="The timeslot you'd like to stream")
    async def c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimBBA CBS Games...")
        await cbb_stream_builder.stream_cbb_game(chan, 'cbs', input, 'c')

    @app_commands.command(name="cbb_d", description="The timeslot you'd like to stream")
    async def d(self, interaction: discord.Integration, input: str):
            chan = self.client.get_channel(channel_id)
            await interaction.response.send_message("Loading SimBBA CBS Games...")
            await cbb_stream_builder.stream_cbb_game(chan, 'cbs', input, 'd')

async def setup(client: commands.Bot):
    await client.add_cog(BBA_Stream(client))