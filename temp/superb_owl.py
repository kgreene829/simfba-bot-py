import discord
from discord.ext import commands
from discord import app_commands
from helper import superb_owl_stream
import settings

channel_id = settings.NFL_STREAM_CHANNEL

class Superb_Owl_Observation(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @app_commands.command(name="sb_q1", description="The timeslot you'd like to stream")
    async def q1(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Superb Owl Observation Q1...")
        await superb_owl_stream.stream_game(chan, 'Q1', input)

    @app_commands.command(name="sb_q2", description="The timeslot you'd like to stream")
    async def q2(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Superb Owl Observation Q2...")
        await superb_owl_stream.stream_game(chan, 'Q2', input)

    @app_commands.command(name="sb_q3", description="The timeslot you'd like to stream")
    async def q3(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Superb Owl Observation Q3...")
        await superb_owl_stream.stream_game(chan, 'Q3', input)

    @app_commands.command(name="sb_q4", description="The timeslot you'd like to stream")
    async def q4(self, interaction: discord.Integration, input: str):
        chan = self.client.get_channel(channel_id)
        await interaction.response.send_message("Superb Owl Observation Q4...")
        await superb_owl_stream.stream_game(chan, 'Q4', input)

async def setup(client: commands.Bot):
    await client.add_cog(Superb_Owl_Observation(client))