import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class nba_player_name_attributes(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="nba_player_name_attributes", description="Look up a profesional basketball player using a {first name}, {last name}, and {team abbreviation}")
    async def nfl_player_name_attributes(self, interaction: discord.Interaction, first_name: str, last_name: str, team_abbreviation: str):
        team_abbreviation = team_abbreviation.upper()
        try:
            team_id = id_util.GetNBATeamID(team_abbreviation)
            logo_url = logos_util.GetNBALogo(team_abbreviation)
            data = api_requests.GetNBABasketballPlayer(first_name, last_name, team_id)
            if data == False:
                await interaction.response.send_message(f"Could not find player")
            else:
                player = data
                title = f"{data['FirstName']} {data['LastName']}"
                desc = f"{player['Year']} year veteran {player['Archetype']} {player['Position']} Graduated from {player['College']}"
                embed = discord.Embed(colour=discord.Colour.orange(),
                                    description=desc,
                                    title=title)

                # Player Attribute Embeds
                embed.add_field(name="Inside Shooting", value=data['Finishing'], inline=True)
                embed.add_field(name="MidRange Shooting", value=data['Shooting2'], inline=True)
                embed.add_field(name="3pt Shooting", value=data['Shooting3'], inline=True)
                embed.add_field(name="Free Throw", value=data['FreeThrow'], inline=True)
                embed.add_field(name="Ballwork", value=data['Ballwork'], inline=True)
                embed.add_field(name="Rebounding", value=data['Rebounding'], inline=True)
                embed.add_field(name="Interior Defense", value=data['InteriorDefense'], inline=True)
                embed.add_field(name="Perimeter Defense", value=data['PerimeterDefense'], inline=True)
                embed.add_field(name="Overall", value=data['Overall'], inline=True)
                embed.add_field(name="Stamina", value=f"{data['Stamina']}", inline=True)
                embed.add_field(name="Potential", value=data['PotentialGrade'], inline=True)
                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(nba_player_name_attributes(client))
