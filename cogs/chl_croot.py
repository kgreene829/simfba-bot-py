import discord
from discord.ext import commands
from discord import app_commands
from helper import croot_hockey_player_builder
import logos_util
import id_util
import api_requests

class chl_croot(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="chl_croot", description="Look up a croot using a croot {id}")
    async def chl_croot(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetCollegeHockeyCroot(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:

                title = f"{data['FirstName']} {data['LastName']} {data['ID']}"
                if {data['City']} == {data['State']}:
                    desc = f"{data['Stars']} Star {data['Archetype']} {data['Position']} from {data['City']}, {data['Country']}"
                else:
                    desc = f"{data['Stars']} Star {data['Archetype']} {data['Position']} from {data['City']}, {data['State']}, {data['Country']}"
                attrlist = croot_hockey_player_builder.GetPriorityFields(data)
                team_id = id_util.GetCollegeHockeyTeamID(data["College"].upper())
                logo_url = logos_util.GetCHLLogo(team_id)
                team = api_requests.GetCollegeHockeyTeam(team_id)
                if team_id != "/":
                    color = team["TeamData"]
                    embed = discord.Embed(colour=discord.Colour.from_str(color["ColorOne"]),
                                    description=desc,
                                    title=title)
                else:
                    embed = discord.Embed(colour=discord.Colour.dark_gold(),
                                    description=desc,
                                    title=title)
                if len(data["RecruitingStatus"]) > 0:
                    embed.add_field(name="Recruiting Status", value=data["RecruitingStatus"], inline=False)
                for x in attrlist:
                    embed.add_field(name=x['name'], value=x['value'], inline=x['inline'])
                embed.add_field(name="", value="", inline=True)
                
                embed.add_field(name="Leading Teams", value="", inline=False)
                leading_teams = data["LeadingTeams"]
                a = 0

                if data['IsSigned'] == True:
                    for i in leading_teams:
                        if leading_teams[a]["Odds"] > 0:
                            embed.add_field(name=leading_teams[a]["TeamAbbr"], value=f"Odds {round(leading_teams[a]['Odds']*100,2)}%", inline=True)
                        a += 1
                else:
                    for i in leading_teams:
                        if leading_teams[a]["Odds"] > 0:
                           odds = round(leading_teams[a]["Odds"]*100,2)
                           if odds > 45:
                               embed.add_field(name=leading_teams[a]["TeamAbbr"], value="Strong Favorite", inline=True)
                           elif odds > 24:
                               embed.add_field(name=leading_teams[a]["TeamAbbr"], value="In Contention", inline=True)
                           elif odds > 11:
                               embed.add_field(name=leading_teams[a]["TeamAbbr"], value="Just Outside", inline=True)
                           else:
                               embed.add_field(name=leading_teams[a]["TeamAbbr"], value="Unlikely", inline=True)
                        a += 1


                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(chl_croot(client))
