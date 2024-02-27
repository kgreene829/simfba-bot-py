import discord
from discord.ext import commands
from discord import app_commands
from helper import player_builder
import logos_util
import id_util
import api_requests

class cfb_player(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cfb_player", description="Look up a college football player using a player {id}")
    async def cfb_player(self, interaction: discord.Interaction, id: str):
        try:
            data = api_requests.GetCollegeFootballPlayer(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided abbreviaton: {id}")
            else:
                title = f"{data['FirstName']} {data['LastName']}"
                desc = f"{data['Stars']} Star {data['Year']} {data['Archetype']} {data['Position']} from {data['City']},{data['State']}"
                attrlist = player_builder.GetPriorityFields(data)
                logo_url = logos_util.GetLogo(data['Team'])
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
    await client.add_cog(cfb_player(client))