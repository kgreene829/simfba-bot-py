import discord
import os
import csv
from helper import embed_builder, message_sender
import constants
import logos_util
import id_util
import asyncio

async def stream_hockey_game(chan, channel: str, week: str, day: str):
    day_uppercase = day.upper()
    injury_url = logos_util.GetIcon("Injury")
    week_directory = os.path.normpath(os.path.join(constants.base_hockey_path, channel, f"Week {week}", day_uppercase))
    play_by_play_directory = os.path.normpath(os.path.join(week_directory, "play_by_plays"))
    if os.path.exists(play_by_play_directory):
        list_of_games = os.listdir(play_by_play_directory)
        for filename in list_of_games:
            contending_teams_str = ""
            home_team_id = ""
            away_team_id = ""
            home_team_abbr = "WISC"
            home_team = ""
            away_team = ""
            away_team_abbr = "UMD"
            final_score = ""
            count = 0
            results = []
            home_coach = "Bundy"
            away_coach = "TuscanSota"
            match_name = "The Winter Classic"
            arena = "Wrigley Field"
            city = "Chicago"
            state = "IL"
            if filename.endswith('.csv'):
                game_path = os.path.normpath(os.path.join(play_by_play_directory, filename))
                with open(game_path, newline="") as game:
                    reader = csv.reader(game, delimiter=",", quotechar='"')
                    total_rows = list(reader)
                    for row in total_rows:
                        if count == 1:
                            count += 1
                            continue
                        elif count == 0:
                            home_team_id = row[1]
                            home_team = row[3].strip()
                            away_team_id = row[5]
                            away_team = row[7].strip()
                            contending_teams_str = f"Home Team: {home_team} | Away Team: {away_team}"
                            final_score = f"{home_team}: 4 | {away_team}: 3"
                            count += 1
                            continue
                        else:
                            score = {
                                "Period": row[0],
                                "Zone": row[3],
                                "Event": row[4],
                                "Outcome": row[5],
                                "Penalty": row[6],
                                "Severity": row[7],
                                "IsFight": row[8],
                                "HomeScore": row[9],
                                "AwayScore": row[10],
                                "TimeOnClock": row[1],
                                "TimeConsumed": row[2],
                                "Result": row[12].strip(),
                                "Possession": row[11]
                            }
                            results.append(score)
                        count += 1

                    ### Logos
                    home_url = logos_util.GetCHLLogo(int(home_team_id))
                    away_url = logos_util.GetCHLLogo(int(away_team_id))

                    ### Build Initial Embed
                    init_embed = discord.Embed(colour=discord.Colour.light_gray(),description=contending_teams_str,title="Streaming College Hockey Game!")
                    if len(match_name) > 0:
                        init_embed.add_field(name="Match Name", value=f"{match_name}", inline=False)
                    init_embed.add_field(name=f"{arena}", value=f"{city}, {state}", inline=False)
                    init_embed.add_field(name=f"Home Coach", value=f"{home_coach}", inline=True)
                    init_embed.add_field(name=f"Away Coach", value=f"{away_coach}", inline=True)
                    init_embed.set_thumbnail(url=home_url)
                    await message_sender.SendEmbedMessage(chan, embed=init_embed)

                    home_score = 0
                    away_score = 0

                    for play in results:
                        time_consumed = play["TimeConsumed"]
                        home_score = play['HomeScore']
                        away_score = play['AwayScore']
                        play_embed = embed_builder.Get_Hockey_Play_Embed(play, home_team_abbr, away_team_abbr, home_url, away_url, home_score, away_score, injury_url)
                        await message_sender.SendEmbedMessage(chan, embed=play_embed)
                        await asyncio.sleep(int(time_consumed))
                    
                    final_title = "... and that's the game, folks! Thank you for watching!"
                    final_url = ""
                    if home_score > away_score:
                        final_url = home_url
                    else:
                        final_url = away_url
                    final_embed = discord.Embed(colour=discord.Colour.light_gray(),description=contending_teams_str,title=final_title)
                    final_embed.add_field(name="Final Score", value=final_score, inline=False)
                    final_embed.set_thumbnail(url=final_url)
                    await message_sender.SendEmbedMessage(chan, embed=final_embed)
                    await asyncio.sleep(10)
                                                

        await chan.send(f"Please tune in on January 18th for more information...")
