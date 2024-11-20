import discord
from discord.ext import commands
from discord import app_commands

class cbbhelp(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cbbhelp", description="Sim introduction and help")
    async def when(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="The CBB can be daunting to jump into, so here are a few useful links for CBB to get you started. We encourage you to explore the dev diary subforum [here](https://www.simfba.com/forum/18-dev-diary/) for detailed explanations in all aspects of the sim and interface. Feel free to also ask for help in the https://discord.com/channels/586207409681334522/1026933570826158231 or in https://discord.com/channels/586207409681334522/850218461480615936.",
                            title="Welcome to the SimCBB brought to you by SimFBA") 
        embed.add_field(name="Gameplanning", value="https://www.simfba.com/topic/4886-94-simcbb-gameplan-update", inline=False)
        embed.add_field(name="Recruiting", value="https://www.simfba.com/topic/3794-72-simbba-interface-recruiting", inline=False)
        embed.add_field(name="Transfers", value="https://www.simfba.com/topic/6216-117-simfba-simbba-transfer-portal-pt-1-high-level-overview", inline=False)
        embed.add_field(name="", value="*Note: Some values and interface layouts may have been updated since these are older dev diaries, but the concepts should mostly stay the same.*", inline=False)
        
        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(cbbhelp(client))
