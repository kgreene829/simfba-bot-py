import discord
from discord.ext import commands
from discord import app_commands
from helper import cfb_stream_builder
import settings

channel_id = settings.NFL_STREAM_CHANNEL

class NFL_Live_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="nfl_thursday_night", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Thursday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Thursday Night Football', input, True)

    @app_commands.command(name="nfl_sunday_noon", description="The timeslot you'd like to stream")
    async def b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Sunday Noon Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Sunday Noon', input, True)

    @app_commands.command(name="nfl_sunday_afternoon", description="The timeslot you'd like to stream")
    async def c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Sunday Afternoon Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Sunday Afternoon', input, True)

    @app_commands.command(name="nfl_sunday_night", description="The timeslot you'd like to stream")
    async def d(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Sunday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Sunday Night Football', input, True)

    @app_commands.command(name="nfl_monday_night", description="The timeslot you'd like to stream")
    async def e(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading SimNFL Monday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'nfl','Monday Night Football', input, True)

async def setup(client: commands.Bot):
    await client.add_cog(NFL_Live_Stream(client))