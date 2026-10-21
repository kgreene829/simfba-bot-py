import discord
import asyncio
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests
import settings

class cbl_class(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cbl_class", description="Look up a college baseball recruiting class using team abbreviation and year")
    async def cbl_class(self, interaction: discord.Interaction, team: str, year: int):
        try:
            await interaction.response.defer()
            a = 0
            upper_input = team.upper()
            team_id = id_util.GetCollegeBaseballTeamID(upper_input)
            year_id = year - 2025
            data = api_requests.GetCollegeBaseballClass(year_id, team_id)
            team_data = api_requests.GetBaseballTeam(team)
            if data == False:
                await interaction.followup.send(f"Could not find class")
            else:
                commitments = data["commitments"]
                title = f"{team_data[0]['team_name']} Recruiting Class"
                desc = f"**Total Recruits:** {data['total']}"
                embed = discord.Embed(colour=discord.Colour.gold(),
                                        description=desc,
                                        title=title)
                embed.set_footer(text="Simulation Sports Network")

                for i in commitments:
                    croot = commitments[a]
                    rank = api_requests.GetBaseballCroot(croot["player_id"], year_id)
                    embed.add_field(name=f"{croot['player_name']} {croot['star_rating']} Star {croot['ptype']} {'Player ' if croot['ptype'] == 'Position' else ''}{croot['player_id']}", value=f"Position Rank: {rank['rank_by_ptype']}\nOverall Rank: {rank['rank_overall']}", inline=False)
                    a+=1

                sorted_fields = sorted(embed.to_dict().get('fields', []), key=lambda field: int(field['value'].split('Overall Rank: ')[1]))
                embed.clear_fields()
                for field in sorted_fields:
                    embed.add_field(name=field['name'], value=field['value'], inline=False)


                await interaction.followup.send(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")
            await interaction.delete_original_response()

async def setup(client: commands.Bot):
    await client.add_cog(cbl_class(client))
