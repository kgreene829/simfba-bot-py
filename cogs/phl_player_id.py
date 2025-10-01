import discord
from discord.ext import commands
from discord import app_commands
from helper import hockey_player_builder
import logos_util
import id_util
import api_requests
import settings

class phl_player_id(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    phl_player_id_group = app_commands.Group(name="phl_player_id", description="PHL Player by ID")


    @phl_player_id_group.command(name="attributes", description="Look up a PHL player using a player {id}")
    async def attributes(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetPHLHockeyPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                title = f"{data['FirstName']} {data['LastName']} {data['PlayerID']}"
                if {data['City']} == {data['State']}:
                    desc = f"{data['Stars']} Star {data['Year']} {data['Archetype']} {data['Position']} from {data['City']}, {data['Country']}"
                else:
                    desc = f"{data['Stars']} Star {data['Year']} {data['Archetype']} {data['Position']} from {data['City']}, {data['State']}, {data['Country']}"
                attrlist = hockey_player_builder.GetPriorityFields(data)
                team_id = id_util.GetPHLTeamID(data['Team'].upper())
                logo_url = logos_util.GetPHLLogo(team_id)
                embed = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                # Player Attribute Embeds
                for x in attrlist:
                    embed.add_field(name=x['name'], value=x['value'], inline=x['inline'])

                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="Simulation Sports Network")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

    
    @phl_player_id_group.command(name="stats", description="Look up a profesional hockey player using a player {id}")
    async def stats(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetPHLHockeyPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                stats = data["ProStats"]
                title = f"{data['FirstName']} {data['LastName']} {data['Position']} {data['PlayerID']}"
                if {data['City']} == {data['State']}:
                    desc = f"{data['Age']} years old {data['Year']} year veteran {data['Archetype']} {data['Position']} from {data['City']}, {data['Country']}"
                else:
                    desc = f"{data['Age']} years old {data['Year']} year veteran {data['Archetype']} {data['Position']} from {data['City']}, {data['State']}, {data['Country']}"
                team_id = id_util.GetPHLTeamID(data['Team'].upper())
                logo_url = logos_util.GetPHLLogo(team_id)
                embed = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)

                if stats["GamesPlayed"] > 0:
                    embed.add_field(name="Games Played", value=stats["GamesPlayed"])
                    if data["Position"] == "G":
                        embed.add_field(name="", value="")
                        embed.add_field(name="", value="")
                        embed.add_field(name="Wins", value=stats["GoalieWins"])
                        embed.add_field(name="Losses", value=stats["GoalieLosses"])
                        embed.add_field(name="Ties", value=stats["GoalieTies"])
                        embed.add_field(name="Overtime Losses", value=stats["OvertimeLosses"])
                        embed.add_field(name="Shots Against", value=stats["ShotsAgainst"])
                        embed.add_field(name="Saves", value=stats["Saves"])
                        embed.add_field(name="Goals Allowed", value=stats["GoalsAgainst"])
                        embed.add_field(name="Save Percentage", value=stats["SavePercentage"])
                        gaa = stats["GoalsAgainst"]/stats["GamesPlayed"]
                        embed.add_field(name="Goals Against Average", value=gaa)
                        embed.add_field(name="Shutouts", value=stats["Shutouts"])
                        if stats["Goals"] > 0:
                            embed.add_field(name="Goals", value=stats["Goals"])
                        if stats["Assists"] > 0:
                            embed.add_field(name="Assists", value=stats["Assists"])
                    else:
                        embed.add_field(name="", value="")
                        embed.add_field(name="Time on Ice", value=stats["TimeOnIce"])
                        if data["Position"] == "C":
                             embed.add_field(name="Faceoffs Taken", value=stats["FaceOffs"])
                             embed.add_field(name="Faceoffs Won", value=stats["FaceOffsWon"])
                             embed.add_field(name="Faceoff Percentage", value=stats["FaceOffWinPercentage"])
                        embed.add_field(name="Goals", value=stats["Goals"])
                        embed.add_field(name="Assists", value=stats["Assists"])
                        embed.add_field(name="Points", value=stats["Points"])
                        if stats["Points"] > stats["EvenStrengthPoints"]:
                            embed.add_field(name="Even Strength Goals", value=stats["EvenStrengthGoals"])
                            eassist = stats["EvenStrengthPoints"]-stats["EvenStrengthGoals"]
                            embed.add_field(name="Even Strength Assists", value=eassist)
                            if stats["PowerPlayPoints"] > 0:
                                embed.add_field(name="Power Play Goals", value=stats["PowerPlayGoals"])
                                passist = stats["PowerPlayPoints"]-stats["PowerPlayGoals"]
                                embed.add_field(name="Power Play Assists", value=passist)
                            if stats["ShorthandedPoints"] > 0:
                                embed.add_field(name="Shorthanded Goals", value=stats["ShorthandedGoals"])
                                sassist = stats["ShorthandedPoints"]-stats["ShorthandedGoals"]
                                embed.add_field(name="Shorthanded Assists", value=sassist)
                        embed.add_field(name="Overtime Goals", value=stats["OvertimeGoals"])
                        embed.add_field(name="Game Winning Goals", value=stats["GameWinningGoals"])
                        embed.add_field(name="Plus/Minus", value=stats["PlusMinus"])
                        embed.add_field(name="Shots", value=stats["Shots"])
                        embed.add_field(name="Shooting Percentage", value=stats["ShootingPercentage"])
                        embed.add_field(name="Shots Blocked", value=stats["ShotsBlocked"])
                        embed.add_field(name="Body Checks", value=stats["BodyChecks"])
                        embed.add_field(name="Stick Checks", value=stats["StickChecks"])
                        embed.add_field(name="PenaltyMinutes", value=stats["PenaltyMinutes"])
                else:
                        embed.add_field(name="",value="Stats work best on players who have actually played games")

                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="Simulation Sports Network")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")



async def setup(client: commands.Bot):
    await client.add_cog(phl_player_id(client))
