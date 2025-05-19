import discord
from discord.ext import commands
from discord import app_commands
from helper import hockey_player_builder
import logos_util
import id_util
import api_requests

class chl_player_name_attributes(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="chl_player_name_attributes", description="Look up a college hockey player using a {first name}, {last name}, and {team}")
    async def chl_player_name_attributes(self, interaction: discord.Interaction, first_name: str, last_name: str, team: str):
        try:
            team_abbreviation = team.upper()
            team_id = id_util.GetCollegeHockeyTeamID(team_abbreviation)
            logo_url = logos_util.GetCHLLogo(team_id)
            data = api_requests.GetCollegeHockeyPlayer(first_name, last_name, team_id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                title = f"{data['FirstName']} {data['LastName']} {data['PlayerID']}"
                if {data['City']} == {data['State']}:
                    desc = f"{data['Stars']} Star {data['Year']} {data['Archetype']} {data['Position']} from {data['City']}, {data['Country']}"
                else:
                    desc = f"{data['Stars']} Star {data['Year']} {data['Archetype']} {data['Position']} from {data['City']}, {data['State']}, {data['Country']}"
                attrlist = hockey_player_builder.GetPriorityFields(data)
                logo_url = logos_util.GetCHLLogo(team_id)
                embed = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                # Player Attribute Embeds
                for x in attrlist:
                    embed.add_field(name=x['name'], value=x['value'], inline=x['inline'])

                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(chl_player_name_attributes(client))
