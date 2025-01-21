import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests

class cfb_player_name_attributes(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cfb_player_name_attributes", description="Look up a college football player using a {first name}, {last name}, and {team}")
    async def cfb_player_name_attributes(self, interaction: discord.Interaction, first_name: str, last_name: str, team: str):
        team_abbreviation = team.upper()
        try:
            team_id = id_util.GetCollegeFootballTeamID(team_abbreviation)
            logo_url = logos_util.GetCFBLogo(team_id)
            data = api_requests.GetCollegeFootballPlayer(first_name, last_name, team_id)
            if data == False:
                await interaction.response.send_message(f"Could not find player")
            else:
                player = data["Player"]
                stats = data["CollegeStats"]
                if stats["ID"] > 0:
                    title = f"{player['FirstName']} {player['LastName']} {stats['CollegePlayerID']}"
                else:
                    title = f"{player['FirstName']} {player['LastName']} {player['Position']}"
                desc = f"{player['Stars']} Star {player['Year']} {player['Archetype']} {player['Position']} from {player['City']}, {player['State']}"
                attrlist = player_builder.GetPriorityFields(player)
                embed_player = discord.Embed(colour=discord.Colour.gold(),
                                    description=desc,
                                    title=title)
                # Player Attribute Embeds
                for x in attrlist:
                    embed_player.add_field(name=x['name'], value=x['value'], inline=x['inline'])

                embed_player.set_thumbnail(url=logo_url)
                embed_player.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed_player)
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(cfb_player_name_attributes(client))
