import json
import os
cbb_abbrevations_json_file = os.path.join("./cbb_abbreviations.json")
cfb_abbrevations_json_file = os.path.join("./cfb_abbreviations.json")
chl_abbrevations_json_file = os.path.join("./chl_abbreviations.json")
nfl_abbrevations_json_file = os.path.join("./nfl_abbreviations.json")
nba_abbrevations_json_file = os.path.join("./nba_abbreviations.json")
phl_abbrevations_json_file = os.path.join("./phl_abbreviations.json")

def GetCollegeHockeyTeamID(abbr):
    with open(chl_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        if abbr in data:
            return data[abbr]
        else:
            no_team = "/"
            return no_team

def GetCollegeBasketballTeamID(abbr):
    with open(cbb_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        if abbr in data:
            return data[abbr]
        else:
            no_team = "/"
            return no_team
    
def GetCollegeFootballTeamID(abbr):
    with open(cfb_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        if abbr in data:
            return data[abbr]
        else:
            no_team = "/"
            return no_team

def GetNFLTeamID(abbr):
    with open(nfl_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        if abbr in data:
            return data[abbr]
        else:
            no_team = "/"
            return no_team

def GetNBATeamID(abbr):
    with open(nba_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        if abbr in data:
            return data[abbr]
        else:
            no_team = "/"
            return no_team

def GetPHLTeamID(abbr):
    with open(phl_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        if abbr in data:
            return data[abbr]
        else:
            no_team = "/"
            return no_team
