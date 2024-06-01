import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class cbb_player_id_attributes(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cbb_player_id_attributes", description="Look up a college basketball player using a player {id}")
    async def cbb_player_id_attributes(self, interaction: discord.Interaction, id: str):
            data = api_requests.GetCollegeBasketballPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                location = ""
                if data['Country'] == 'USA':
                    location = data['State']
                else:
                    location = data['Country']
                title = f"{data['FirstName']} {data['LastName']}"
                desc = f"{data['Stars']} Star {data['Archetype']} {data['Position']} from {location}"
                logo_url = logos_util.GetLogo(data['TeamAbbr'])

                embed = discord.Embed(colour=discord.Colour.orange(),
                                    description=desc,
                                    title=title)

                # Player Attribute Embeds
                embed.add_field(name="Inside Shooting", value=data['FinishingGrade'], inline=True)
                embed.add_field(name="MidRange Shooting", value=data['Shooting2Grade'], inline=True)
                embed.add_field(name="3pt Shooting", value=data['Shooting3Grade'], inline=True)
                embed.add_field(name="Free Throw", value=data['FreeThrowGrade'], inline=True)
                embed.add_field(name="Ballwork", value=data['BallworkGrade'], inline=True)
                embed.add_field(name="Rebounding", value=data['ReboundingGrade'], inline=True)
                embed.add_field(name="Interior Defense", value=data['InteriorDefenseGrade'], inline=True)
                embed.add_field(name="Perimeter Defense", value=data['PerimeterDefenseGrade'], inline=True)
                embed.add_field(name="Overall", value=data['OverallGrade'], inline=True)
                embed.add_field(name="Stamina", value=f"{data['Stamina']}", inline=True)
                embed.add_field(name="Potential", value=data['PotentialGrade'], inline=True)
                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(cbb_player_id_attributes(client))
