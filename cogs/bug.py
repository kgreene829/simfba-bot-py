import discord
from discord.ext import commands
from discord import app_commands

class bug(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="bug", description="If you notice a bug please report it to either Kgreene829 or Tuscansota on discord")
    async def when(self, interaction: discord.Interaction):
        embed = discord.Embed(colour=discord.Colour.dark_gold(),
                            description="If you notice a bug please report it to either Kgreene829 or Tuscansota through DMs on discord.",
                            title="Did you find a bug in the bot?")
        embed.add_field(name="Kgreene829", value="Please reach out to Kgreene829 first especially for minor bugs", inline=False)
        embed.add_field(name="We thank you for your help in continuing to improve the discord bot.", value="", inline=False)
        
        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(bug(client))
