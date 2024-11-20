import discord
from discord.ext import commands
from discord import app_commands

class simhelp(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="simhelp", description="Sim introduction and help")
    async def when(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="But first, who are we, and what is SimFBA all about?",
                            title="Welcome to SimFBA! We're excited to have you join us on your adventure to becoming a successful coach!")
        embed.add_field(name="", value="Read our mission and rules [here](https://www.simfba.com/topic/3-simulation-football-association-mission-statement-about-and-rules).", inline=False)
        embed.add_field(name="", value="If you still find this interesting, learn how to apply for a team [here](https://www.simfba.com/topic/2-read-here-first-new-member-application)!", inline=False)
        embed.add_field(name="", value="Create an account [here](https://www.simfba.com/forum/6-job-applications-and-interviews) to see an updated list of available teams.", inline=False)
        embed.add_field(name="", value="This interface will also serve as the location for box scores, team management, recruiting, and many other ways to interact with your team.", inline=False)        
        
        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(simhelp(client))
