import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests

class cfb_croot(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cfb_croot", description="Look up a croot using a croot {id}")
    async def cfb_croot(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetCollegeFootballCroot(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:

                title = f"{data['FirstName']} {data['LastName']} {id}"
                desc = f"{data['Stars']} Star {data['Archetype']} {data['Position']} from {data['City']}, {data['State']}"
                team_id = id_util.GetCollegeFootballTeamID(data["College"].upper())
                logo_url = logos_util.GetCFBLogo(team_id)
                embed = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                embed.add_field(name="Overall", value=data["OverallGrade"], inline=True)
                embed.add_field(name="Potential", value=data["PotentialGrade"], inline=True)
                embed.add_field(name="Recruiting Status", value=data["RecruitingStatus"], inline=True)
                embed.add_field(name="Personality", value=data["Personality"], inline=True)
                embed.add_field(name="Recruiting Bias", value=data["RecruitingBias"], inline=True)
                embed.add_field(name="Academic Bias", value=data["AcademicBias"], inline=True)
                embed.add_field(name="Work Ethic", value=data["WorkEthic"], inline=False)
                
                embed.add_field(name="Leading Teams", value="", inline=False)
                leading_teams = data["LeadingTeams"]
                a = 0
                
                for i in leading_teams:
                    if leading_teams[a]["Odds"] > 0:
                        embed.add_field(name=leading_teams[a]["TeamAbbr"], value=f"Odds {round(leading_teams[a]['Odds']*100,2)}%", inline=True)
                        
                    a += 1

                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(cfb_croot(client))
