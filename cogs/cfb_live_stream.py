import discord
from discord.ext import commands
from discord import app_commands
from helper import cfb_stream_builder
import settings

channel_id = settings.STREAM_CHANNEL
big_noon_id = settings.B1G_NOON
after_dark_id = settings.AFTER_DARK
prime_time = settings.PRIME_TIME

class FBS_Stream(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="fbs_thursday", description="The timeslot you'd like to stream")
    async def a(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FBS Thursday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fbs', 'Thursday Night', input, False)

    @app_commands.command(name="fbs_friday", description="The timeslot you'd like to stream")
    async def b(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FBS Friday Night Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fbs', 'Friday Night', input, False)

    @app_commands.command(name="fbs_saturday_morning", description="The timeslot you'd like to stream")
    async def c(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Loading FBS Saturday Morning Games...")
        await cfb_stream_builder.stream_fb_game(chan, 'fbs','Saturday Morning', input, False)

    @app_commands.command(name="fbs_saturday_afternoon", description="The timeslot you'd like to stream")
    async def e(self, interaction: discord.Integration, input: str):
            chan = self.client.get_channel(big_noon_id)
            await interaction.response.send_message("Loading FBS Saturday Afternoon Games...")
            await cfb_stream_builder.stream_fb_game(chan, 'fbs','Saturday Afternoon', input, False)

    @app_commands.command(name="fbs_saturday_evening", description="The timeslot you'd like to stream")
    async def f(self, interaction: discord.Integration, input: str):
            chan = self.client.get_channel(prime_time)
            await interaction.response.send_message("Loading FBS Saturday Evening Games...")
            await cfb_stream_builder.stream_fb_game(chan, 'fbs','Saturday Evening', input, False)    
    
    @app_commands.command(name="fbs_saturday_night", description="The timeslot you'd like to stream")
    async def g(self, interaction: discord.Integration, input: str):
            chan = self.client.get_channel(after_dark_id)
            await interaction.response.send_message("Loading Pac-2 After Dark...")
            await cfb_stream_builder.stream_fb_game(chan, 'fbs','Saturday Night', input, False)

async def setup(client: commands.Bot):
    await client.add_cog(FBS_Stream(client))