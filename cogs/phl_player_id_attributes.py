import discord
from discord.ext import commands
from discord import app_commands
from helper import hockey_player_builder
import logos_util
import id_util
import api_requests

class phl_player_id_attributes(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="phl_player_id_attributes", description="Look up a PHL player using a player {id}")
    async def phl_player_id_attributes(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetPHLHockeyPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                title = f"{data['FirstName']} {data['LastName']} {data['PlayerID']}"
                if {data['City']} == {data['State']}:
                    desc = f"{data['Stars']} Star {data['Year']} {data['Archetype']} {data['Position']} from {data['City']}, {data['Country']}"
                else:
                    desc = f"{data['Stars']} Star {data['Year']} {data['Archetype']} {data['Position']} from {data['City']}, {data['State']}, {data['Country']}"
                attrlist = hockey_player_builder.GetPriorityFields(data)
                team_id = id_util.GetPHLTeamID(data['Team'].upper())
                logo_url = logos_util.GetPHLLogo(team_id)
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
    await client.add_cog(phl_player_id_attributes(client))
