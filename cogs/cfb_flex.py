import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class cfb_flex(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cfb_flex", description="Compare the wins between two CFB Programs. Input two {teams}")
    async def cfb_flex(self, interaction: discord.Integration, t1: str, t2: str):
        t1_upper = t1.upper()
        t2_upper = t2.upper()
        team_one_id = id_util.GetCollegeFootballTeamID(t1_upper)
        team_two_id = id_util.GetCollegeFootballTeamID(t2_upper)
        data = api_requests.CompareTwoCFBTeams(team_one_id, team_two_id)
        if data == False:
            await interaction.response.send_message(f"Could not find team based on the provided teams: {t1} {t2}")
        else:
            latest_win = data["LatestWin"]
            team_id = id_util.GetCollegeFootballTeamID(data["LatestWin"].upper())
            latest_win_url = logos_util.GetCFBLogo(team_id)
            current_streak = data["CurrentStreak"]
            team_one_wins = data["TeamOneWins"]
            team_one_losses = data["TeamOneLosses"]
            team_one_streak = data["TeamOneStreak"]
            team_one_season = data["TeamOneMSeason"]
            team_one_margin_score = data["TeamOneMScore"]
            team_two_wins = data["TeamTwoWins"]
            team_two_losses = data["TeamTwoLosses"]
            team_two_streak = data["TeamTwoStreak"]
            team_two_season = data["TeamTwoMSeason"]
            team_two_margin_score = data["TeamTwoMScore"]
            title = f"Comparison Between {t1} and {t2}"
            desc = f"Current Streak: {latest_win} with {current_streak} wins"
            embed = discord.Embed(colour=discord.Colour.dark_gold(),
                                description=desc,
                                title=title)
            embed.add_field(name=f"{t1} Wins", value=team_one_wins, inline=True)
            embed.add_field(name=f"{t1} Losses", value=team_one_losses, inline=True)
            embed.add_field(name=f"{t1} Best Streak", value=team_one_streak, inline=True)
            if team_one_season > 0:
                embed.add_field(name=f"{t1} Largest Margin of Victory", value=f"{team_one_margin_score}, {team_one_season}", inline=True)
            embed.add_field(name="\u200B", value="\u200B")
            embed.add_field(name=f"{t2} Wins", value=team_two_wins, inline=True)
            embed.add_field(name=f"{t2} Losses", value=team_two_losses, inline=True)
            embed.add_field(name=f"{t2} Best Streak", value=team_two_streak, inline=True)
            if team_two_season > 0:
                embed.add_field(name=f"{t2} Largest Margin of Victory", value=f"{team_two_margin_score}, {team_two_season}", inline=True)
            embed.set_thumbnail(url=latest_win_url)
            await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(cfb_flex(client))
