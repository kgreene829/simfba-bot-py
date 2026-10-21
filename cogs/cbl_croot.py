import discord
import asyncio
from discord.ext import commands
from discord import app_commands
import logos_util
import api_requests
import settings

class cbl_croot(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    @app_commands.command(name="cbl_croot", description="Look up a college baseball recruit using player id and year")
    async def cbl_croot(self, interaction: discord.Interaction, id: str, year: int):
        try:
            await interaction.response.defer()
            year_id = year - 2025
            data = api_requests.GetBaseballCroot(id, year_id)
            try:
                team = data["commitment"]["org_id"]
                committed = True
                scout = api_requests.GetBaseballCrootCommitted(id, year_id, team)
            except Exception as e:
                committed = False
                scout = api_requests.GetBaseballCrootCommitted(id, year_id)
            bio = scout["bio"]
            if data == False:
                await interaction.followup.send(f"Could not find croot")
            else:
                title = f"{data['player_name']} {data['player_id']}"
                desc = f"{data['star_rating']} Star {data['ptype']} {'Player ' if data['ptype'] == 'Position' else ''}from {bio['city']}, {bio['area']}"
                embed = discord.Embed(colour=discord.Colour.gold(),
                                        description=desc,
                                        title=title)
                embed.set_footer(text="Simulation Sports Network")

                if data["ptype"] == "Position":
                    batting = scout["generated_stats"]["batting"]
                    fielding = scout["generated_stats"]["fielding"]
                    if committed == True:
                        embed.add_field(name="Committed To", value=data["commitment"]["org_abbrev"])
                    embed.add_field(name="Games Played", value=batting["games"])
                    embed.add_field(name="At Bats", value=batting["at_bats"])
                    embed.add_field(name="Batting Average", value=batting["avg"])
                    embed.add_field(name="OBP", value=batting["obp"])
                    embed.add_field(name="Slugging", value=batting["slg"])
                    embed.add_field(name="OPS", value=f"{batting['obp']+batting['slg']:.3f}")
                    embed.add_field(name="Hits", value=batting["hits"])
                    embed.add_field(name="Doubles", value=batting["doubles"])
                    embed.add_field(name="Triples", value=batting["triples"])
                    embed.add_field(name="Home Runs", value=batting["home_runs"])
                    embed.add_field(name="Strike Outs", value=batting["strikeouts"])
                    embed.add_field(name="Walks", value=batting["walks"])
                    embed.add_field(name="Runs", value=batting["runs"])
                    embed.add_field(name="RBI", value=batting["rbi"])
                    embed.add_field(name="Stolen Bases", value=batting["stolen_bases"])
                    embed.add_field(name="Caught Stealing", value=batting["caught_stealing"])
                    embed.add_field(name="Defensive Innings", value=fielding["innings"])
                    embed.add_field(name="Fielding Percentage", value=f"{round(fielding['fielding_pct']*100,2)}%")
                    embed.add_field(name="Putouts", value=fielding["putouts"])
                    embed.add_field(name="Assists", value=fielding["assists"])
                    embed.add_field(name="Errors", value=fielding["errors"])
                    if committed == True:
                        if scout["visibility"]["unlocked"]:
                            report = scout["text_report"]
                            embed.add_field(name="Athletic Scouting Report", value=report["athletic"])
                            embed.add_field(name="Batting Scouting Report", value=report["batting"])
                            embed.add_field(name="Fielding Scouting Report", value=report["fielding"])

                else:
                    pitching = scout["generated_stats"]["pitching"]
                    if committed == True:
                        embed.add_field(name="Committed To", value=data["commitment"]["org_abbrev"])
                    embed.add_field(name="Games Played", value=pitching["games"])
                    embed.add_field(name="Games Started", value=pitching["games_started"])
                    embed.add_field(name="Innings Pitched", value=pitching["innings_pitched"])
                    embed.add_field(name="Record", value=f"{pitching['wins']}-{pitching['losses']}")
                    embed.add_field(name="Saves", value=pitching["saves"])
                    embed.add_field(name="Earned Runs", value=pitching["earned_runs"])
                    embed.add_field(name="ERA", value=pitching["era"])
                    embed.add_field(name="WHIP", value=pitching["whip"])
                    embed.add_field(name="Strike Outs", value=pitching["strikeouts"])
                    embed.add_field(name="Walks", value=pitching["walks"])
                    embed.add_field(name="Walks Per 9", value=pitching["bb_per_9"])
                    embed.add_field(name="Hits Allowed", value=pitching["hits_allowed"])
                    embed.add_field(name="Home Runs Allowed", value=pitching["home_runs_allowed"])
                    if committed == True:
                        if scout["visibility"]["unlocked"]:
                            report = scout["text_report"]
                            embed.add_field(name="Athletic Scouting Report", value=report["athletic"])
                            embed.add_field(name="Batting Scouting Report", value=report["batting"])
                            embed.add_field(name="Fielding Scouting Report", value=report["fielding"])
                            embed.add_field(name="Pitching Scouting Report", value=report["pitching"])

                await interaction.followup.send(embed=embed)
                
        except Exception as e:
            print(f"Error occured: {e}")

async def setup(client: commands.Bot):
    await client.add_cog(cbl_croot(client))
