import discord
from discord.ext import commands
from discord import app_commands

class nbahelp(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="nbahelp", description="Sim introduction and help")
    async def when(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="The NBA can be daunting to jump into, so here are a few useful links for NBA to get you started. We encourage you to explore the dev diary subforum [here](https://www.simfba.com/forum/18-dev-diary/) for detailed explanations in all aspects of the sim and interface. Feel free to also ask for help in the https://discord.com/channels/586207409681334522/1026933591919317133 or in https://discord.com/channels/586207409681334522/850218461480615936.",
                            title="Welcome to the SimNBA brought to you by SimFBA") 
        embed.add_field(name="Gameplanning", value="https://www.simfba.com/topic/4886-94-simcbb-gameplan-update", inline=False)
        embed.add_field(name="Free Agency", value="https://www.simfba.com/topic/7521-129-simfba-simbba-offseason-free-agency-update", inline=False)
        embed.add_field(name="Drafting", value="https://www.simfba.com/topic/5441-100-the-simnba-draft-page", inline=False)
        embed.add_field(name="", value="*Note: Some values and interface layouts may have been updated since these are older dev diaries, but the concepts should mostly stay the same.*", inline=False)
        
        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(nbahelp(client))
