import discord
from discord.ext import commands
from discord import app_commands
from helper import toucan_facts_list
import random

class toucan_facts(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="toucan_facts", description="Want to learn more about toucans?")
    async def when(self, interaction: discord.Interaction):
        fact_list = toucan_facts_list.GetToucanFactsList()
        message = random.choice(fact_list)
        await interaction.response.send_message(message)

async def setup(client: commands.Bot):
    await client.add_cog(toucan_facts(client))