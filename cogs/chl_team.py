import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class chl_team(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        
    @app_commands.command(name="chl_team", description="Look up a college hockey team")
    async def chl_team(self, interaction: discord.Interaction, team: str):
        upper_input = team.upper()
        team_id = id_util.GetCollegeHockeyTeamID(upper_input)
        logo_url = logos_util.GetCHLLogo(team_id)
        data = api_requests.GetCollegeHockeyTeam(team_id)
        if data == False:
            await interaction.response.send_message(f"Could not find team: {input}")
        else:
            team_data = data["TeamData"]
            standings = data["TeamStandings"]
            matches = data["UpcomingMatches"]
            rank = standings['Rank']
            rank_label = ""
            if rank > 0:
                rank_label = f"({rank})"
            title = f"{rank_label} {team_data['TeamName']} {team_data['Mascot']}"
            desc = f"University based in {team_data['City']}, {team_data['State']}. Members of the {team_data['Conference']}."
            embed = discord.Embed(colour=discord.Colour.from_str(team_data["ColorOne"]),
                                description=desc,
                                title=title)
            coach = ""
            if len(team_data['Coach']) > 0:
                coach = team_data['Coach']
            else:
                coach = "AI"
            embed.add_field(name="Coach", value=coach, inline=False)
            embed.add_field(name="Arena", value=team_data['Arena'], inline=False)
            if len(standings['PostSeasonStatus']) > 0:
                embed.add_field(name="Post-Season Status", value=standings['PostSeasonStatus'], inline=True)
            current_record_label = f"{standings['TotalWins']}-{standings['TotalLosses']} ({standings['ConferenceWins']}-{standings['ConferenceLosses']})"
            embed.add_field(name="Current Record", value=f"{current_record_label}", inline=True)

            if len(matches) > 0:
                embed.add_field(name="\u200B", value="\u200B")
                for m in matches:
                    is_complete = m['GameComplete']
                    match_description = ""
                    neutral_label = ""
                    conf_label = ""
                    playoff_label = ""
                    natty_label = ""
                    match_arena = f"{m['Arena']}"
                    ovr_desc = ""
                    if is_complete == True:
                        match_description = f"{m['AwayTeamScore']}-{m['HomeTeamScore']}"
                    else:
                        match_description = f"{m['Week']} {m['GameDay']} "
                    if m['IsNeutralSite'] == True:
                        neutral_label = 'Neutral Site '
                    if m['IsConference'] == True:
                        conf_label = 'Conference Matchup'
                    if m['IsPlayoffGame'] == True:
                        playoff_label = 'Playoff Matchup '
                    if m['IsNationalChampionship'] == True:
                        natty_label = 'National Championship'
                    ovr_desc = f"{match_description} | {neutral_label}{conf_label}{playoff_label}{natty_label} At {match_arena}"
                    opposing_coach_label = ""
                    if m['AwayTeamID'] == team_id:
                        opposing_coach_label = f"{m['HomeTeamCoach']}"
                    else:
                        opposing_coach_label = f"{m['AwayTeamCoach']}"

                    a_rank_label = ''
                    h_rank_label = ''
                    if m['AwayTeamRank'] > 0:
                        a_rank_label = f"({m['AwayTeamRank']})"
                    if m['HomeTeamRank'] > 0:
                        h_rank_label = f"({m['HomeTeamRank']})"
                    m_name_label = f"{a_rank_label} {m['AwayTeam']} at {h_rank_label} {m['HomeTeam']} | VS {opposing_coach_label}"
                    embed.add_field(name=m_name_label, value=ovr_desc, inline=False)
            
            embed.set_thumbnail(url=logo_url)
            await interaction.response.send_message(embed=embed)
            
async def setup(client: commands.Bot):
    await client.add_cog(chl_team(client))
