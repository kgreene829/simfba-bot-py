import discord
### FOR STREAMING

def Get_CBB_Play_Embed(play, home_abbr, away_abbr, home_url, away_url, home_score, away_score):
    type_of_play = play["TypeOfPlay"]
    time_remaining = play["TimeRemaining"]
    possession = play["Possession"]
    result = play["Result"]
    desc = f"Current Score: {home_abbr} {home_score} - {away_abbr} {away_score}"
    embed_url = ""
    if possession == home_abbr:
        embed_url = home_url
    else:
        embed_url = away_url
    embed = discord.Embed(colour=discord.Colour.orange(),description=desc,title="Play")
    embed.add_field(name="Type of Play", value=f"{type_of_play}", inline=False)
    embed.add_field(name=f"Possessions Remaining: {time_remaining}", value=f"Possession: {possession}", inline=False)
    embed.add_field(name="Result", value=f"{result}", inline=False)    
    embed.set_thumbnail(url=embed_url)
    return embed

def Get_FBA_Play_Embed(play, home_abbr, away_abbr, home_url, away_url, home_score, away_score):
    type_of_play = play["TypeOfPlay"]
    time_remaining = play["TimeRemaining"]
    possession = play["Possession"]
    result = play["Result"]
    distance = play["Distance"]
    down_input = play["Down"]
    down = get_down(down_input)
    line_of_scrimmage = play["LineOfScrimmage"]
    desc = f"Current Score: {home_abbr} {home_score} - {away_abbr} {away_score}"
    embed_url = ""
    home_abbr_arr = home_abbr.split(" ")
    if possession == home_abbr_arr[0]:
        embed_url = home_url
    else:
        embed_url = away_url
    embed = discord.Embed(colour=discord.Colour.dark_gold(),description=desc,title="Play")
    embed.add_field(name=f"Possessions Remaining: {time_remaining}", value=f"Possession: {possession}", inline=False)
    embed.add_field(name=f"{down} and {distance}", value=f"Line of Scrimmage: {line_of_scrimmage}", inline=False)
    embed.add_field(name="Type of Play", value=f"{type_of_play}", inline=False)
    embed.add_field(name="Result", value=f"{result}", inline=False)    
    embed.set_thumbnail(url=embed_url)
    return embed

def get_down(down):
    if down == "1":
        return "1st Down"
    elif down == "2":
        return "2nd Down"
    elif down == "3":
        return "3rd Down"
    elif down == "4":
        return "4th Down"
    return "IT'S 5TH DOWN EVERYBODY!"