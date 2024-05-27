import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests

class cfb_player(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cfb_player", description="Look up a college football player using a player {id}")
    async def cfb_player(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetCollegeFootballPlayer(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided abbreviaton: {id}")
            else:
                player = data["Player"]
                stats = data["CollegeStats"]
                title = f"{player['FirstName']} {player['LastName']}"
                desc = f"{player['Stars']} Star {player['Year']} {player['Archetype']} {player['Position']} from {player['City']},{player['State']}"
                attrlist = player_builder.GetPriorityFields(player)
                logo_url = logos_util.GetLogo(player['Team'])
                embed_player = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                # Player Attribute Embeds
                for x in attrlist:
                    embed_player.add_field(name=x['name'], value=x['value'], inline=x['inline'])
                if stats["ID"] > 0:
                    # Add the relevant stats on the season
                    if stats["GamesPlayed"] >0:
                        embed_player.add_field(name="Games Played", value=stats["GamesPlayed"], inline=x['inline'])
                    if stats["PassAttempts"] > 0:
                        embed_player.add_field(name="Pass Completions", value=stats["PassCompletions"], inline=x['inline'])
                        embed_player.add_field(name="Pass Attempts", value=stats["PassAttempts"], inline=x['inline'])
                        embed_player.add_field(name="Passing Yards", value=stats["PassingYards"], inline=x['inline'])
                        embed_player.add_field(name="Passing Avg", value=stats["PassingAvg"], inline=x['inline'])
                        embed_player.add_field(name="Pass TDs", value=stats["PassingTDs"], inline=x['inline'])
                        embed_player.add_field(name="INTs", value=stats["Interceptions"], inline=x['inline'])
                        embed_player.add_field(name="QB Sacks", value=stats["Sacks"], inline=x['inline'])
                        embed_player.add_field(name="Longest Pass", value=stats["LongestPass"], inline=x['inline'])
                        embed_player.add_field(name="QBR", value=stats["QBRating"], inline=x['inline'])
                    if stats["RushAttempts"] >0:
                        embed_player.add_field(name="Rushing Yards", value=stats["RushingYards"], inline=x['inline'])
                        embed_player.add_field(name="Rush Attempts", value=stats["RushAttempts"], inline=x['inline'])
                        embed_player.add_field(name="Rushing Avg", value=stats["RushingAvg"], inline=x['inline'])
                        embed_player.add_field(name="Rushing TDs", value=stats["RushingTDs"], inline=x['inline'])
                        embed_player.add_field(name="Longest Rush", value=stats["LongestRush"], inline=x['inline'])

                    if stats["Targets"] >0:
                        embed_player.add_field(name="Receiving Yards", value=stats["ReceivingYards"], inline=x['inline'])
                        embed_player.add_field(name="Catches", value=stats["Catches"], inline=x['inline'])
                        embed_player.add_field(name="Targets", value=stats["Targets"], inline=x['inline'])
                        embed_player.add_field(name="Rec. TDs", value=stats["ReceivingTDs"], inline=x['inline'])
                        embed_player.add_field(name="Longest Rec.", value=stats["LongestReception"], inline=x['inline'])

                    if stats["Fumbles"] > 0:
                        embed_player.add_field(name="Fumbles", value=stats["Fumbles"], inline=x['inline'])

                    if stats["Tackles"] >0:
                        embed_player.add_field(name="Tackles", value=stats["Tackles"], inline=x['inline'])
                        embed_player.add_field(name="Asst. Tackles", value=stats["AssistedTackles"], inline=x['inline'])
                        embed_player.add_field(name="TFL", value=stats["TacklesForLoss"], inline=x['inline'])
                        embed_player.add_field(name="Sacks", value=stats["SacksMade"], inline=x['inline'])
                        embed_player.add_field(name="FF", value=stats["ForcedFumbles"], inline=x['inline'])
                        embed_player.add_field(name="FR", value=stats["RecoveredFumbles"], inline=x['inline'])
                    if stats["PassDeflections"] >0:
                        embed_player.add_field(name="Pass Deflections", value=stats["PassDeflections"], inline=x['inline'])
                    if stats["InterceptionsCaught"] >0:
                        embed_player.add_field(name="INTs", value=stats["InterceptionsCaught"], inline=x['inline'])
                    if stats["Safeties"] >0:
                        embed_player.add_field(name="Safeties", value=stats["Safeties"], inline=x['inline'])
                    if stats["DefensiveTDs"] >0:
                        embed_player.add_field(name="Defensive TDs", value=stats["DefensiveTDs"], inline=x['inline'])
                    if stats["FGAttempts"] >0:
                        embed_player.add_field(name="FG Made", value=stats["FGMade"], inline=x['inline'])
                        embed_player.add_field(name="FG Attempts", value=stats["FGAttempts"], inline=x['inline'])
                        embed_player.add_field(name="Longest FG", value=stats["LongestFG"], inline=x['inline'])
                    if stats["ExtraPointsAttempted"] >0:
                        embed_player.add_field(name="XP Made", value=stats["ExtraPointsMade"], inline=x['inline'])
                        embed_player.add_field(name="XP Attempts", value=stats["ExtraPointsAttempted"], inline=x['inline'])
                    if stats["Punts"] >0:
                        embed_player.add_field(name="Punts", value=stats["Punts"], inline=x['inline'])
                        embed_player.add_field(name="Net Punt Distance", value=stats["NetPuntDistance"], inline=x['inline'])
                        embed_player.add_field(name="Grs. Punt Distance", value=stats["GrossPuntDistance"], inline=x['inline'])
                        embed_player.add_field(name="Punt Touchbacks", value=stats["PuntTouchbacks"], inline=x['inline'])
                        embed_player.add_field(name="Inside 20", value=stats["PuntsInside20"], inline=x['inline'])

                embed_player.set_thumbnail(url=logo_url)
                embed_player.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed_player)
        except Exception as e:
            print(f"Error occured: {e}")

    @app_commands.command(name="nfl_player", description="Look up a professional football player using a player {id}")
    async def nfl_player(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetNFLFootballPlayer(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided abbreviaton: {id}")
            else:
                player = data["Player"]
                stats = data["NFLStats"]
                title = f"{player['FirstName']} {player['LastName']}"
                desc = f"{player['Year']} Year {player['Archetype']} {player['Position']} Graduated from {player['College']}"
                attrlist = player_builder.GetPriorityFields(player)
                logo_url = logos_util.GetLogo(player['Team'])
                embed_player = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                # Player Attribute Embeds
                for x in attrlist:
                    embed_player.add_field(name=x['name'], value=x['value'], inline=x['inline'])
                if stats["ID"] > 0:
                    # Add the relevant stats on the season
                    if stats["GamesPlayed"] >0:
                        embed_player.add_field(name="Games Played", value=stats["GamesPlayed"], inline=x['inline'])
                    if stats["PassAttempts"] > 0:
                        embed_player.add_field(name="Pass Completions", value=stats["PassCompletions"], inline=x['inline'])
                        embed_player.add_field(name="Pass Attempts", value=stats["PassAttempts"], inline=x['inline'])
                        embed_player.add_field(name="Passing Yards", value=stats["PassingYards"], inline=x['inline'])
                        embed_player.add_field(name="Passing Avg", value=stats["PassingAvg"], inline=x['inline'])
                        embed_player.add_field(name="Pass TDs", value=stats["PassingTDs"], inline=x['inline'])
                        embed_player.add_field(name="INTs", value=stats["Interceptions"], inline=x['inline'])
                        embed_player.add_field(name="QB Sacks", value=stats["Sacks"], inline=x['inline'])
                        embed_player.add_field(name="Longest Pass", value=stats["LongestPass"], inline=x['inline'])
                        embed_player.add_field(name="QBR", value=stats["QBRating"], inline=x['inline'])
                    if stats["RushAttempts"] >0:
                        embed_player.add_field(name="Rushing Yards", value=stats["RushingYards"], inline=x['inline'])
                        embed_player.add_field(name="Rush Attempts", value=stats["RushAttempts"], inline=x['inline'])
                        embed_player.add_field(name="Rushing Avg", value=stats["RushingAvg"], inline=x['inline'])
                        embed_player.add_field(name="Rushing TDs", value=stats["RushingTDs"], inline=x['inline'])
                        embed_player.add_field(name="Longest Rush", value=stats["LongestRush"], inline=x['inline'])

                    if stats["Targets"] >0:
                        embed_player.add_field(name="Receiving Yards", value=stats["ReceivingYards"], inline=x['inline'])
                        embed_player.add_field(name="Catches", value=stats["Catches"], inline=x['inline'])
                        embed_player.add_field(name="Targets", value=stats["Targets"], inline=x['inline'])
                        embed_player.add_field(name="Rec. TDs", value=stats["ReceivingTDs"], inline=x['inline'])
                        embed_player.add_field(name="Longest Rec.", value=stats["LongestReception"], inline=x['inline'])

                    if stats["Fumbles"] > 0:
                        embed_player.add_field(name="Fumbles", value=stats["Fumbles"], inline=x['inline'])

                    if stats["Tackles"] >0:
                        embed_player.add_field(name="Tackles", value=stats["Tackles"], inline=x['inline'])
                        embed_player.add_field(name="Asst. Tackles", value=stats["AssistedTackles"], inline=x['inline'])
                        embed_player.add_field(name="TFL", value=stats["TacklesForLoss"], inline=x['inline'])
                        embed_player.add_field(name="Sacks", value=stats["SacksMade"], inline=x['inline'])
                        embed_player.add_field(name="FF", value=stats["ForcedFumbles"], inline=x['inline'])
                        embed_player.add_field(name="FR", value=stats["RecoveredFumbles"], inline=x['inline'])
                    if stats["PassDeflections"] >0:
                        embed_player.add_field(name="Pass Deflections", value=stats["PassDeflections"], inline=x['inline'])
                    if stats["InterceptionsCaught"] >0:
                        embed_player.add_field(name="INTs", value=stats["InterceptionsCaught"], inline=x['inline'])
                    if stats["Safeties"] >0:
                        embed_player.add_field(name="Safeties", value=stats["Safeties"], inline=x['inline'])
                    if stats["DefensiveTDs"] >0:
                        embed_player.add_field(name="Defensive TDs", value=stats["DefensiveTDs"], inline=x['inline'])
                    if stats["FGAttempts"] >0:
                        embed_player.add_field(name="FG Made", value=stats["FGMade"], inline=x['inline'])
                        embed_player.add_field(name="FG Attempts", value=stats["FGAttempts"], inline=x['inline'])
                        embed_player.add_field(name="Longest FG", value=stats["LongestFG"], inline=x['inline'])
                    if stats["ExtraPointsAttempted"] >0:
                        embed_player.add_field(name="XP Made", value=stats["ExtraPointsMade"], inline=x['inline'])
                        embed_player.add_field(name="XP Attempts", value=stats["ExtraPointsAttempted"], inline=x['inline'])
                    if stats["Punts"] >0:
                        embed_player.add_field(name="Punts", value=stats["Punts"], inline=x['inline'])
                        embed_player.add_field(name="Net Punt Distance", value=stats["NetPuntDistance"], inline=x['inline'])
                        embed_player.add_field(name="Grs. Punt Distance", value=stats["GrossPuntDistance"], inline=x['inline'])
                        embed_player.add_field(name="Punt Touchbacks", value=stats["PuntTouchbacks"], inline=x['inline'])
                        embed_player.add_field(name="Inside 20", value=stats["PuntsInside20"], inline=x['inline'])

                embed_player.set_thumbnail(url=logo_url)
                embed_player.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed_player)
        except Exception as e:
            await interaction.response.send_message(f"Could not find player: {id}")
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(cfb_player(client))