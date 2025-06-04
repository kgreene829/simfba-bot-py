import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class nba_player_id(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    nba_player_id_group = app_commands.Group(name="nba_player_id", description="NBA Player by ID")

    @nba_player_id_group.command(name="attributes", description="Look up a profesional basketball player using a player {id}")
    async def attributes(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetNBABasketballPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                title = f"{data['FirstName']} {data['LastName']} {data['Position']}"
                desc = f"{data['Year']} year veteran {data['Archetype']} {data['Position']} Graduated from {data['College']}"
                team_id = id_util.GetNBATeamID(data['TeamAbbr'].upper())
                logo_url = logos_util.GetNBALogo(team_id)
                embed = discord.Embed(colour=discord.Colour.orange(),
                                description=desc,
                                title=title)

                # Player Attribute Embeds
                embed.add_field(name="Overall", value=data['Overall'], inline=True)
                embed.add_field(name="Experience", value=data['Year'], inline=True)
                embed.add_field(name="Position", value=data['Position'], inline=True)
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
                embed.set_footer(text="Simulation Sports Network")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            await interaction.response.send_message(f"Could not find player: {id}")
            print(f"Error occured: {e}")


    @nba_player_id_group.command(name="stats", description="Look up a profesional basketball player using a player {id}")
    async def stats(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetNBABasketballPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                stats = data["SeasonStats"]
                title = f"{data['FirstName']} {data['LastName']} {data['Position']}"
                desc = f"{data['Year']} year veteran {data['Archetype']} {data['Position']} Graduated from {data['College']}"
                team_id = id_util.GetNBATeamID(data['TeamAbbr'].upper())
                logo_url = logos_util.GetNBALogo(team_id)
                embed = discord.Embed(colour=discord.Colour.orange(),
                                description=desc,
                                title=title)

                # Player Stats Embeds
                embed.add_field(name="Games Played", value=stats['GamesPlayed'], inline=True)
                embed.add_field(name="Minutes Per Game", value=stats['MinutesPerGame'], inline=True)
                embed.add_field(name="Possessions Per Game", value=stats['PossessionsPerGame'], inline=True)
                embed.add_field(name="FGs Attempted", value=stats['FGA'], inline=True)
                embed.add_field(name="FGs Made", value=stats['FGM'], inline=True)
                try:
                    embed.add_field(name="FG %", value=str(round((stats['FGM']/stats['FGA'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="FG %", value="N/A", inline=True)
                embed.add_field(name="3 Pointers Attempted", value=stats['ThreePointAttempts'], inline=True)
                embed.add_field(name="3 Pointers Made", value=stats['ThreePointsMade'], inline=True)
                try:
                    embed.add_field(name="3 Point %", value=str(round((stats['ThreePointsMade']/stats['ThreePointAttempts'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="3 Point %", value="N/A", inline=True)
                embed.add_field(name="FTs Attempted", value=stats['FTA'], inline=True)
                embed.add_field(name="FTs Made", value=stats['FTM'], inline=True)
                try:
                    embed.add_field(name="FT %", value=str(round((stats['FTM']/stats['FTA'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="FT %", value="N/A", inline=True)
                embed.add_field(name="Offensive Rebounds", value=stats['OffRebounds'], inline=True)
                embed.add_field(name="Defensiv Rebounds", value=stats['DefRebounds'], inline=True)
                embed.add_field(name="Total Rebounds", value=stats['TotalRebounds'], inline=True)
                embed.add_field(name="Assists", value=stats['Assists'], inline=True)
                embed.add_field(name="Steals", value=stats['Steals'], inline=True)
                embed.add_field(name="Blocks", value=stats['Blocks'], inline=True)
                embed.add_field(name="Turnovers", value=stats['Turnovers'], inline=True)
                embed.add_field(name="Fouls", value=stats['Fouls'], inline=True)
                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="Simulation Sports Network")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")



async def setup(client: commands.Bot):
    await client.add_cog(nba_player_id(client))
