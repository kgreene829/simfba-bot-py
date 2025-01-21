import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests

class nfl_player_name_attributes(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="nfl_player_name_attributes", description="Look up a profesional football player using a {first name}, {last name}, and {team}")
    async def nfl_team(self, interaction: discord.Interaction, first_name: str, last_name: str, team: str):
        abbr = team.upper()
        try:
            team_id = id_util.GetNFLTeamID(abbr)
            logo_url = logos_util.GetNFLLogo(team_id)
            data = api_requests.GetNFLFootballPlayer(first_name, last_name, team_id)
            if data == False:
                await interaction.response.send_message(f"Could not find player")
            else:
                player = data["Player"]
                stats = data["NFLStats"]
                if stats["ID"] > 0:
                    title = f"{player['FirstName']} {player['LastName']} {player['Position']}"
                else:
                    title = f"{player['FirstName']} {player['LastName']} {player['Position']}"
                desc = f"{player['Year']} year veteran {player['Archetype']} {player['Position']} Graduated from {player['College']}"
                attrlist = player_builder.GetPriorityFields(player)
                logo_url = logos_util.GetLogo(player['Team'])
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
    await client.add_cog(nfl_player_name_attributes(client))
