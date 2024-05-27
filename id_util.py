import json
import os
cbb_abbrevations_json_file = os.path.join("./cbb_abbreviations.json")
cfb_abbrevations_json_file = os.path.join("./cfb_abbreviations.json")
nfl_abbrevations_json_file = os.path.join("./nfl_abbreviations.json")

def GetCollegeBasketballTeamID(abbr):
    with open(cbb_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        return data[abbr]
    
def GetCollegeFootballTeamID(abbr):
    with open(cfb_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        return data[abbr]

def GetNFLTeamID(abbr):
    with open(nfl_abbrevations_json_file, 'r') as f:
        data = json.load(f)
        return data[abbr]