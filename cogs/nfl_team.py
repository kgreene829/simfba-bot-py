import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class nfl_team(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="nfl_team", description="Look up a professional football team")
    async def nfl_team(self, interaction: discord.Interaction, input: str):
        upper_input = input.upper()
        team_id = id_util.GetNFLTeamID(upper_input)
        logo_url = logos_util.GetNFLLogo(upper_input)
        data = api_requests.GetNFLFootballTeam(team_id)
        if data == False:
            await interaction.response.send_message(f"Could not find team based on the provided abbreviaton: {input}")
        else:
            team_data = data["Team"]
            title = f"{team_data['TeamName']} {team_data['Mascot']}"
            desc = f"Team based in {team_data['City']}, {team_data['State']}. Members of the {team_data['Conference']} {team_data['Division']}."
            embed = discord.Embed(colour=discord.Colour.dark_gold(),
                                description=desc,
                                title=title)
            owner = ""
            if len(team_data['NFLOwnerName']) > 0:
                owner = team_data['NFLOwnerName']
            else:
                owner = "AI"
                
            gm = ""
            if len(team_data['NFLGMName']) > 0:
                gm = team_data['NFLGMName']
            else:
                gm = "AI"
            coach = ""
            if len(team_data['NFLCoachName']) > 0:
                coach = team_data['NFLCoachName']
            else:
                coach = "AI"
            assistant = ""
            if len(team_data['NFLAssistantName']) > 0:
                assistant = team_data['NFLAssistantName']
            else:
                assistant = "AI"

            if owner != "AI":
                embed.add_field(name="Owner", value=owner, inline=True)
            if gm != "AI":
                embed.add_field(name="GM", value=gm, inline=True)
            if coach != "AI":
                embed.add_field(name="Coach", value=coach, inline=True)
            if assistant != "AI":
                embed.add_field(name="Assistant", value=assistant, inline=True)
            embed.add_field(name="Stadium", value=team_data['Stadium'], inline=False)
            a_rank_label = ''
            h_rank_label = ''
    
            embed.set_thumbnail(url=logo_url)
            await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(nfl_team(client))
