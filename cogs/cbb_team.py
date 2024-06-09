import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class cbb_team(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cbb_team", description="Look up a college basketball team")
    async def cbb_team(self, interaction: discord.Integration, team: str):
        upper_input = team.upper()
        team_id = id_util.GetCollegeBasketballTeamID(upper_input)
        logo_url = logos_util.GetLogo(team_id)
        data = api_requests.GetCollegeBasketballTeam(team_id)
        if data == False:
            await interaction.response.send_message(f"Could not find team based on the provided abbreviaton: {input}")
        else:
            team_data = data["TeamData"]
            standings = data["TeamStandings"]
            matches = data["UpcomingMatches"]
            title = f"{team_data['Team']} {team_data['Nickname']}"
            desc = f"University based in {team_data['City']}, {team_data['State']}. Members of the {team_data['Conference']}."
            embed = discord.Embed(colour=discord.Colour.orange(),
                                description=desc,
                                title=title)
            coach = ""
            if len(team_data['Coach']) > 0:
                coach = team_data['Coach']
            else:
                coach = "AI"
            embed.add_field(name="Coach", value=coach, inline=False)
            embed.add_field(name="Arena", value=team_data['Arena'], inline=False)
            embed.add_field(name="Overall", value=team_data['OverallGrade'], inline=True)
            embed.add_field(name="Offense", value=team_data['OffenseGrade'], inline=True)
            embed.add_field(name="Defense", value=team_data['DefenseGrade'], inline=True)
            if len(standings['PostSeasonStatus']) > 0:
                embed.add_field(name="Post-Season Status", value=standings['PostSeasonStatus'], inline=True)
            if standings['IsConferenceChampion'] == True:
                embed.add_field(name=f"{standings['ConferenceName']} Champion", value=f"For the {standings['Season']} Season", inline=True)
            if standings['InvitationalParticipant'] == True:
                invi_label = ""
                if standings['InvitationalChampion'] == True:
                    invi_label = "Champion"
                else:
                    invi_label = "Participant"
                embed.add_field(name=f"{standings['Invitational']}", value=f"{invi_label}", inline=True)
            current_record_label = f"{standings['TotalWins']}-{standings['TotalLosses']} ({standings['ConferenceWins']}-{standings['ConferenceLosses']})"
            embed.add_field(name="Current Record", value=f"{current_record_label}", inline=True)

            if len(matches) > 0:
                embed.add_field(name="\u200B", value="\u200B")
                for m in matches:
                    is_complete = m['GameComplete']
                    match_description = ""
                    neutral_label = ""
                    conf_label = ""
                    conf_tourney_label = ""
                    nit_label =""
                    playoff_label = ""
                    natty_label = ""
                    match_arena = f"{m['Arena']}"
                    ovr_desc = ""
                    if is_complete == True:
                        match_description = f"{m['AwayTeamScore']}-{m['HomeTeamScore']}"
                    else:
                        match_description = f"{m['Week']}{m['MatchOfWeek']}"
                    if m['IsNeutralSite'] == True:
                        neutral_label = 'Neutral Site '
                    if m['IsConference'] == True:
                        conf_label = 'Conference Matchup'
                    if m['IsConferenceTournament'] == True:
                        conf_tourney_label = 'Conference Tournament Matchup '
                    if m['IsNITGame'] == True:
                        nit_label = 'NIT Matchup '
                    if m['IsPlayoffGame'] == True:
                        playoff_label = 'Playoff Matchup '
                    if m['IsNationalChampionship'] == True:
                        natty_label = 'National Championship'
                    ovr_desc = f"{match_description} | {neutral_label}{conf_label}{conf_tourney_label}{nit_label}{playoff_label}{natty_label} At {match_arena}"
                    opposing_coach_label = ""
                    if m['AwayTeamID'] == team_id:
                        opposing_coach_label = f"{m['HomeTeamCoach']}"
                    else:
                        opposing_coach_label = f"{m['AwayTeamCoach']}"
                    m_name_label = f"{m['AwayTeam']} at {m['HomeTeam']} | VS {opposing_coach_label}"
                    embed.add_field(name=m_name_label, value=ovr_desc, inline=False)
            
            embed.set_thumbnail(url=logo_url)
            await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(cbb_team(client))
