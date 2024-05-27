import discord
from discord.ext import commands
from discord import app_commands
from helper import cfb_stream_builder
import settings

channel_id = settings.FCS_STREAM_CHANNEL

class FCS_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="fcs_thursday", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FCS Thursday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fcs', 'Thursday Night', input, False)

    @app_commands.command(name="fcs_friday", description="The timeslot you'd like to stream")
    async def b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FCS Friday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fcs', 'Friday Night', input, False)

    @app_commands.command(name="fcs_saturday_morning", description="The timeslot you'd like to stream")
    async def c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FCS Saturday Morning Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fcs','Saturday Morning', input, False)

    @app_commands.command(name="fcs_saturday_afternoon", description="The timeslot you'd like to stream")
    async def e(self, interaction: discord.Integration, input: str):
            chan = self.client.get_channel(channel_id)
            await interaction.response.send_message("Loading FCS Saturday Afternoon Games...")
            await cfb_stream_builder.stream_fb_game(chan, 'fcs','Saturday Afternoon', input, False)

    @app_commands.command(name="fcs_saturday_evening", description="The timeslot you'd like to stream")
    async def f(self, interaction: discord.Integration, input: str):
            chan = self.client.get_channel(channel_id)
            await interaction.response.send_message("Loading FCS Saturday Evening Games...")
            await cfb_stream_builder.stream_fb_game(chan, 'fcs','Saturday Evening', input, False)    
    
    @app_commands.command(name="fcs_saturday_night", description="The timeslot you'd like to stream")
    async def g(self, interaction: discord.Integration, input: str):
            chan = self.client.get_channel(channel_id)
            await interaction.response.send_message("Loading Big Sky After Dark...")
            await cfb_stream_builder.stream_fb_game(chan, 'fcs','Saturday Night', input, False)

async def setup(client: commands.Bot):
    await client.add_cog(FCS_Stream(client))