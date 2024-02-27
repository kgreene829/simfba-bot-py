import discord
import os
import csv
from helper import embed_builder
import constants
import logos_util
import asyncio

async def stream_game(chan, quarter: str, year: str):
    game_directory = os.path.normpath(os.path.join(constants.base_superb_owl_path, f"Year {year}", quarter))
    if os.path.exists(game_directory):
        games_files = os.listdir(game_directory)
        for file in games_files:
            file_name = file.replace(" Play-By-Play.csv", "")
            teams = file_name.split(" vs ")
            home_team_name = teams[0]
            away_team_name = teams[1]
            if file.endswith('Play-By-Play.csv'):
                game_file_path = os.path.normpath(os.path.join(game_directory, file))
                with open(game_file_path, newline="") as game:
                    reader = csv.reader(game, delimiter=",", quotechar="|")
                    total_rows = list(reader)
                    contending_teams_str = ""
                    final_score = ""
                    count = 0
                    results = []
                    scheme_string = ""
                    for row in total_rows:
                        if count == 0:
                            home_team_abbr = row[0].strip()
                            away_team_abbr = row[1].strip()
                            contending_teams_str = f"Home Team: {home_team_abbr} | Away Team: {away_team_abbr}"
                        elif count == 1:
                            contending_teams_str += f"\nHome Coach: {row[1].strip()} | Away Coach: {row[3].strip()}"
                        elif count == 2:
                            scheme_string = f"Home Offensive Scheme: {row[1].strip()} | Away Offensive Scheme: {row[3].strip()}"
                        elif count == 3:
                            scheme_string += f"\nHome Defensive Scheme: {row[1].strip()} | Away Defensive Scheme: {row[3].strip()}"
                        elif count == 4:
                            final_score = f"{home_team_abbr}: {row[1]} | {away_team_abbr}: {row[3].strip()}"
                        elif count == 5 or count == len(total_rows) - 1:
                            ...
                        else:
                            score = {
                                "HomeScore": row[0],
                                "AwayScore": row[1],
                                "Quarter": row[2],
                                "TimeRemaining": row[3],
                                "Down": row[5],
                                "Distance": row[6],
                                "LineOfScrimmage": row[7],
                                "TypeOfPlay": row[8],
                                "Result": row[9].strip(),
                                "Possession": row[4]
                            }
                            results.append(score)
                        count += 1

                    ### Logos
                    home_url = logos_util.GetLogo(home_team_name.strip())
                    away_url = logos_util.GetLogo(away_team_name.strip())

                    ### Build Initial Embed
                    init_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title="Streaming SimNFL Match!")
                    init_embed.add_field(name="Schemes", value=scheme_string, inline=False)
                    init_embed.set_thumbnail(url=home_url)
                    await chan.send(embed=init_embed)

                    await asyncio.sleep(10)

                    home_score = 0
                    away_score = 0

                    for play in results:
                        home_score = play['HomeScore']
                        away_score = play['AwayScore']
                        play_embed = embed_builder.Get_FBA_Play_Embed(play, home_team_name, away_team_name, home_url, away_url, home_score, away_score)
                        await chan.send(embed=play_embed)
                        await asyncio.sleep(30)
                    
                    final_url = ""
                    if home_score > away_score:
                        final_url = home_url
                    else:
                        final_url = away_url
                    final_score_title = "Final Score"
                    final_title = "... and that's the game, folks! Thank you for watching!"
                    if quarter == "Q1":
                        final_score_title = "Current Score"
                        final_title ="... and that's the end of the 1st Quarter Folks! Tune in shortly as the second quarter begins soon!"
                        final_score = f"{home_team_abbr}: {home_score} | {away_team_abbr}: {away_score}"
                    if quarter == "Q2":
                        final_score_title = "Current Score"
                        final_score = f"{home_team_abbr}: {home_score} | {away_team_abbr}: {away_score}"
                        final_title ="... and that brings us to half time, folks! Tune in for our halftime as we break down the first half and interview coaches!"
                    if quarter == "Q3":
                        final_score_title = "Current Score"
                        final_score = f"{home_team_abbr}: {home_score} | {away_team_abbr}: {away_score}"
                        final_title ="... and that's the end of the 3rd Quarter Folks! Tune in shortly for the final quarter and the grand finale to this excellent matchup!"
                    final_embed = discord.Embed(colour=discord.Colour.blue(),description=contending_teams_str,title=final_title)
                    final_embed.add_field(name=final_score_title, value=final_score, inline=False)
                    final_embed.set_thumbnail(url=final_url)
                    await chan.send(embed=final_embed)
                    await asyncio.sleep(30)