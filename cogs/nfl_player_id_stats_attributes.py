import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests

class nfl_player_id_attributes(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="nfl_player_id_attributes", description="Look up a professional football player using a player {id}")
    async def nfl_player_id_attributes(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetNFLFootballPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                player = data["Player"]
                stats = data["NFLStats"]
                title = f"{player['FirstName']} {player['LastName']} {player['Position']}"
                desc = f"{player['Year']} year veteran {player['Archetype']} {player['Position']} Graduated from {player['College']}"
                attrlist = player_builder.GetPriorityFields(player)
                team_id = id_util.GetNFLTeamID(player['Team'].upper())
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
            await interaction.response.send_message(f"Could not find player: {id}")
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(nfl_player_id_attributes(client))
