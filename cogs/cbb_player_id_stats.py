import discord
from discord.ext import commands
from discord import app_commands
import logos_util
import id_util
import api_requests

class cbb_player_id_stats(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cbb_player_id_stats", description="Look up a college basketball player using a player {id}")
    async def cbb_player_id_stats(self, interaction: discord.Interaction, id: str):
            data = api_requests.GetCollegeBasketballPlayer_id(id)
            if data == False:
                await interaction.response.send_message(f"Could not find player based on the provided id: {id}")
            else:
                location = ""
                if data['Country'] == 'USA':
                    location = data['State']
                else:
                    location = data['Country']
                stats = data["SeasonStats"]
                title = f"{data['FirstName']} {data['LastName']} {str(id)}"
                desc = f"{data['Stars']} Star {data['Archetype']} {data['Position']} from {location}"
                logo_url = logos_util.GetLogo(data['TeamAbbr'])

                embed = discord.Embed(colour=discord.Colour.orange(),
                                    description=desc,
                                    title=title)

                # Player Stats Embeds
                embed.add_field(name="Games Played", value=stats['GamesPlayed'], inline=True)
                embed.add_field(name="Minutes Per Game", value=stats['MinutesPerGame'], inline=True)
                embed.add_field(name="Possessions Per Game", value=stats['PossessionsPerGame'], inline=True)
                embed.add_field(name="FGs Attempted", value=stats['FGA'], inline=True)
                embed.add_field(name="FGs Made", value=stats['FGM'], inline=True)
                try:
                    embed.add_field(name="FG %", value=str(round((stats['FGM']/stats['FGA'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="FG %", value="N/A", inline=True)
                embed.add_field(name="3 Pointers Attempted", value=stats['ThreePointAttempts'], inline=True)
                embed.add_field(name="3 Pointers Made", value=stats['ThreePointsMade'], inline=True)
                try:
                    embed.add_field(name="3 Point %", value=str(round((stats['ThreePointsMade']/stats['ThreePointAttempts'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="3 Point %", value="N/A", inline=True)
                embed.add_field(name="FTs Attempted", value=stats['FTA'], inline=True)
                embed.add_field(name="FTs Made", value=stats['FTM'], inline=True)
                try:
                    embed.add_field(name="FT %", value=str(round((stats['FTM']/stats['FTA'])*100,2))+"%", inline=True)
                except Exception as e:
                    embed.add_field(name="FT %", value="N/A", inline=True)
                embed.add_field(name="Offensive Rebounds", value=stats['OffRebounds'], inline=True)
                embed.add_field(name="Defensiv Rebounds", value=stats['DefRebounds'], inline=True)
                embed.add_field(name="Total Rebounds", value=stats['TotalRebounds'], inline=True)
                embed.add_field(name="Assists", value=stats['Assists'], inline=True)
                embed.add_field(name="Steals", value=stats['Steals'], inline=True)
                embed.add_field(name="Blocks", value=stats['Blocks'], inline=True)
                embed.add_field(name="Turnovers", value=stats['Turnovers'], inline=True)
                embed.add_field(name="Fouls", value=stats['Fouls'], inline=True)
                embed.set_thumbnail(url=logo_url)
                embed.set_footer(text="SimFBA Association")
                await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(cbb_player_id_stats(client))
