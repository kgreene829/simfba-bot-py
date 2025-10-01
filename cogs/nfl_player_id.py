import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests
import settings

class nfl_player_id(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    nfl_player_id_group = app_commands.Group(name="nfl_player_id", description="NFL Player by ID")


    @nfl_player_id_group.command(name="attributes", description="Look up a professional football player using a player {id}")
    async def attributes(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetNFLFootballPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                player = data["Player"]
                stats = data["NFLStats"]
                title = f"{player['FirstName']} {player['LastName']} {player['Position']}"
                desc = f"{player['Year']} year veteran {player['Archetype']} {player['Position']} Graduated from {player['College']}"
                attrlist = player_builder.GetPriorityFields(player)
                team_id = id_util.GetNFLTeamID(player['Team'].upper())
                logo_url = logos_util.GetNFLLogo(team_id)
                embed_player = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                
                # Player Attribute Embeds
                for x in attrlist:
                    embed_player.add_field(name=x['name'], value=x['value'], inline=x['inline'])

                embed_player.set_thumbnail(url=logo_url)
                embed_player.set_footer(text="Simulation Sports Network")
                await interaction.response.send_message(embed=embed_player)
        except Exception as e:
            await interaction.response.send_message(f"Could not find player: {id}")
            print(f"Error occured: {e}")


    @nfl_player_id_group.command(name="stats", description="Look up a professional football player using a player {id}")
    async def stats(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetNFLFootballPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                player = data["Player"]
                stats = data["NFLStats"]
                title = f"{player['FirstName']} {player['LastName']} {player['Position']}"
                desc = f"{player['Year']} year veteran {player['Archetype']} {player['Position']} Graduated from {player['College']}"
                attrlist = player_builder.GetPriorityFields(player)
                team_id = id_util.GetNFLTeamID(player['Team'].upper())
                logo_url = logos_util.GetNFLLogo(team_id)
                embed_player = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                
                if stats["ID"] > 0:
                    # Add the relevant stats on the season
                    if stats["GamesPlayed"] >0:
                        embed_player.add_field(name="Games Played", value=stats["GamesPlayed"])
                    if stats["PassAttempts"] > 0:
                        embed_player.add_field(name="Pass Completions", value=stats["PassCompletions"])
                        embed_player.add_field(name="Pass Attempts", value=stats["PassAttempts"])
                        embed_player.add_field(name="Passing Yards", value=stats["PassingYards"])
                        embed_player.add_field(name="Passing Avg", value=round(stats["PassingAvg"],2))
                        embed_player.add_field(name="Pass TDs", value=stats["PassingTDs"])
                        embed_player.add_field(name="INTs", value=stats["Interceptions"])
                        embed_player.add_field(name="QB Sacks", value=stats["Sacks"])
                        embed_player.add_field(name="Longest Pass", value=stats["LongestPass"])
                        embed_player.add_field(name="QBR", value=round(stats["QBRating"],2))
                        
                    if stats["RushAttempts"] >0:
                        embed_player.add_field(name="Rushing Yards", value=stats["RushingYards"])
                        embed_player.add_field(name="Rush Attempts", value=stats["RushAttempts"])
                        embed_player.add_field(name="Rushing Avg", value=round(stats["RushingAvg"],2))
                        embed_player.add_field(name="Rushing TDs", value=stats["RushingTDs"])
                        embed_player.add_field(name="Longest Rush", value=stats["LongestRush"])
                        
                    if stats["Targets"] >0:
                        embed_player.add_field(name="Receiving Yards", value=stats["ReceivingYards"])
                        embed_player.add_field(name="Catches", value=stats["Catches"])
                        embed_player.add_field(name="Targets", value=stats["Targets"])
                        embed_player.add_field(name="Rec. TDs", value=stats["ReceivingTDs"])
                        embed_player.add_field(name="Longest Rec.", value=stats["LongestReception"])

                    if stats["Fumbles"] > 0:
                        embed_player.add_field(name="Fumbles", value=stats["Fumbles"])

                    if stats["Tackles"] >0:
                        embed_player.add_field(name="Tackles", value=stats["Tackles"])
                        embed_player.add_field(name="Asst. Tackles", value=stats["AssistedTackles"])
                        embed_player.add_field(name="TFL", value=stats["TacklesForLoss"])
                        embed_player.add_field(name="Sacks", value=stats["SacksMade"])
                        embed_player.add_field(name="FF", value=stats["ForcedFumbles"])
                        embed_player.add_field(name="FR", value=stats["RecoveredFumbles"])
                    if stats["PassDeflections"] >0:
                        embed_player.add_field(name="Pass Deflections", value=stats["PassDeflections"])
                    if stats["InterceptionsCaught"] >0:
                        embed_player.add_field(name="INTs", value=stats["InterceptionsCaught"])
                    if stats["Safeties"] >0:
                        embed_player.add_field(name="Safeties", value=stats["Safeties"])
                    if stats["DefensiveTDs"] >0:
                        embed_player.add_field(name="Defensive TDs", value=stats["DefensiveTDs"])
                    if stats["FGAttempts"] >0:
                        embed_player.add_field(name="FG Made", value=stats["FGMade"])
                        embed_player.add_field(name="FG Attempts", value=stats["FGAttempts"])
                        '''
                        FG%
                        embed_player.add_field(name="FG Percentage", value=str(round((stats["FGMade"]/stats["FGAttempts"])*100,2))+"%")
                        '''
                        embed_player.add_field(name="Longest FG", value=stats["LongestFG"])
                    if stats["ExtraPointsAttempted"] >0:
                        embed_player.add_field(name="XP Made", value=stats["ExtraPointsMade"])
                        embed_player.add_field(name="XP Attempts", value=stats["ExtraPointsAttempted"])
                        '''
                        XP%
                        embed_player.add_field(name="XP Percentage", value=str(round((stats["ExtraPointsMade"]/stats["ExtraPointsAttempted"])*100,2))+"%")
                        '''
                    if stats["Punts"] >0:
                        embed_player.add_field(name="Punts", value=stats["Punts"])
                        embed_player.add_field(name="Net Punt Distance", value=stats["NetPuntDistance"])
                        embed_player.add_field(name="Grs. Punt Distance", value=stats["GrossPuntDistance"])
                        embed_player.add_field(name="Punt Touchbacks", value=stats["PuntTouchbacks"])
                        embed_player.add_field(name="Inside 20", value=stats["PuntsInside20"])

                else:
                    embed_player.add_field(name="Stats work best on players who have actually played games", value = "")

                embed_player.set_thumbnail(url=logo_url)
                embed_player.set_footer(text="Simulation Sports Network")
                await interaction.response.send_message(embed=embed_player)
        except Exception as e:
            await interaction.response.send_message(f"Could not find player: {id}")
            print(f"Error occured: {e}")

    @nfl_player_id_group.command(name="career_stats", description="Look up a professional football player using a player {id}")
    async def career_stats(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetNFLFootballPlayerCareer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                player = data["Player"]
                stats = data["NFLStats"]
                title = f"{player['FirstName']} {player['LastName']} {player['Position']}"
                desc = f"{player['Year']} year veteran {player['Archetype']} {player['Position']} Graduated from {player['College']}"
                attrlist = player_builder.GetPriorityFields(player)
                team_id = id_util.GetNFLTeamID(player['Team'].upper())
                logo_url = logos_util.GetNFLLogo(team_id)
                embed_player = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                
                    # Add the relevant stats on the season
                if stats["GamesPlayed"] >0:
                    embed_player.add_field(name="Games Played", value=stats["GamesPlayed"])
                    if stats["PassAttempts"] > 0:
                        embed_player.add_field(name="Pass Completions", value=stats["PassCompletions"])
                        embed_player.add_field(name="Pass Attempts", value=stats["PassAttempts"])
                        embed_player.add_field(name="Passing Yards", value=stats["PassingYards"])
                        embed_player.add_field(name="Passing Avg", value=round(stats["PassingAvg"],2))
                        embed_player.add_field(name="Pass TDs", value=stats["PassingTDs"])
                        embed_player.add_field(name="INTs", value=stats["Interceptions"])
                        embed_player.add_field(name="QB Sacks", value=stats["Sacks"])
                        embed_player.add_field(name="Longest Pass", value=stats["LongestPass"])
                        embed_player.add_field(name="QBR", value=round(stats["QBRating"],2))
                        
                    if stats["RushAttempts"] >0:
                        embed_player.add_field(name="Rushing Yards", value=stats["RushingYards"])
                        embed_player.add_field(name="Rush Attempts", value=stats["RushAttempts"])
                        embed_player.add_field(name="Rushing Avg", value=round(stats["RushingAvg"],2))
                        embed_player.add_field(name="Rushing TDs", value=stats["RushingTDs"])
                        embed_player.add_field(name="Longest Rush", value=stats["LongestRush"])
                        
                    if stats["Targets"] >0:
                        embed_player.add_field(name="Receiving Yards", value=stats["ReceivingYards"])
                        embed_player.add_field(name="Catches", value=stats["Catches"])
                        embed_player.add_field(name="Targets", value=stats["Targets"])
                        embed_player.add_field(name="Rec. TDs", value=stats["ReceivingTDs"])
                        embed_player.add_field(name="Longest Rec.", value=stats["LongestReception"])

                    if stats["Fumbles"] > 0:
                        embed_player.add_field(name="Fumbles", value=stats["Fumbles"])

                    if stats["Tackles"] >0:
                        embed_player.add_field(name="Tackles", value=stats["Tackles"])
                        embed_player.add_field(name="Asst. Tackles", value=stats["AssistedTackles"])
                        embed_player.add_field(name="TFL", value=stats["TacklesForLoss"])
                        embed_player.add_field(name="Sacks", value=stats["SacksMade"])
                        embed_player.add_field(name="FF", value=stats["ForcedFumbles"])
                        embed_player.add_field(name="FR", value=stats["RecoveredFumbles"])
                    if stats["PassDeflections"] >0:
                        embed_player.add_field(name="Pass Deflections", value=stats["PassDeflections"])
                    if stats["InterceptionsCaught"] >0:
                        embed_player.add_field(name="INTs", value=stats["InterceptionsCaught"])
                    if stats["Safeties"] >0:
                        embed_player.add_field(name="Safeties", value=stats["Safeties"])
                    if stats["DefensiveTDs"] >0:
                        embed_player.add_field(name="Defensive TDs", value=stats["DefensiveTDs"])
                    if stats["FGAttempts"] >0:
                        embed_player.add_field(name="FG Made", value=stats["FGMade"])
                        embed_player.add_field(name="FG Attempts", value=stats["FGAttempts"])
                        '''
                        FG%
                        embed_player.add_field(name="FG Percentage", value=str(round((stats["FGMade"]/stats["FGAttempts"])*100,2))+"%")
                        '''
                        embed_player.add_field(name="Longest FG", value=stats["LongestFG"])
                    if stats["ExtraPointsAttempted"] >0:
                        embed_player.add_field(name="XP Made", value=stats["ExtraPointsMade"])
                        embed_player.add_field(name="XP Attempts", value=stats["ExtraPointsAttempted"])
                        '''
                        XP%
                        embed_player.add_field(name="XP Percentage", value=str(round((stats["ExtraPointsMade"]/stats["ExtraPointsAttempted"])*100,2))+"%")
                        '''
                    if stats["Punts"] >0:
                        embed_player.add_field(name="Punts", value=stats["Punts"])
                        embed_player.add_field(name="Net Punt Distance", value=stats["NetPuntDistance"])
                        embed_player.add_field(name="Grs. Punt Distance", value=stats["GrossPuntDistance"])
                        embed_player.add_field(name="Punt Touchbacks", value=stats["PuntTouchbacks"])
                        embed_player.add_field(name="Inside 20", value=stats["PuntsInside20"])

                else:
                    embed_player.add_field(name="Stats work best on players who have actually played games")

                embed_player.set_thumbnail(url=logo_url)
                embed_player.set_footer(text="Simulation Sports Network")
                await interaction.response.send_message(embed=embed_player)
        except Exception as e:
            await interaction.response.send_message(f"Could not find player: {id}")
            print(f"Error occured: {e}")


async def setup(client: commands.Bot):
    await client.add_cog(nfl_player_id(client))
