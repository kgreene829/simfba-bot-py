import requests
import json

fba_url = "https://simfba.azurewebsites.net/"
test_url = "http://localhost:5001/"
bba_url = "https://simnba.azurewebsites.net/"

def GetCollegeBasketballTeam(id):
    res = requests.get(f"{bba_url}dis/cbb/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeBasketballPlayer(first_name, last_name, id):
    res = requests.get(f"{bba_url}dis/cbb/player/{first_name}/{last_name}/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetAllCBBMatches():
    res = requests.get(f"{bba_url}match/season/3")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballPlayer(id):
    res = requests.get(f"{fba_url}ds/cfb/player/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetNFLFootballPlayer(id):
    res = requests.get(f"{fba_url}ds/nfl/player/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballPlayerIndStats(id, week):
    res = requests.get(f"{fba_url}ds/cfb/player/indstats/{id}/{week}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballPlayerSeasonStats(id):
    res = requests.get(f"{fba_url}ds/cfb/player/seasonsstats/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballCroot(id):
    res = requests.get(f"{fba_url}ds/cfb/croot/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballCrootingClass(id):
    res = requests.get(f"{fba_url}ds/cfb/croots/class/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballConfStandings(id):
    res = requests.get(f"{fba_url}ds/cfb/conference/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def GetCollegeFootballTeam(id):
    res = requests.get(f"{fba_url}ds/cfb/team/{id}")
    if res.status_code == 200:
        return res.json()
    return False

def CompareTwoCFBTeams(t1, t2):
    res = requests.get(f"{fba_url}ds/cfb/flex/{t1}/{t2}")
    if res.status_code == 200:
        return res.json()
    return False

def StreamFootballGames(league, timeslot, week, isNFL):
    req_url = ""
    if isNFL == False:
        req_url = f"{fba_url}ds/cfb/{league}/stream/{timeslot}/{week}/"
    else:
        req_url = f"{fba_url}ds/nfl/league/stream/{timeslot}/{week}/"
    res = requests.get(f"{req_url}")
    if res.status_code == 200:
        return res.json()
    return False

def RegisterFBTeam(isNFL, team_id, user):
    req_url = ""
    if isNFL == False:
        req_url = f"{fba_url}ds/cfb/assign/discord/{team_id}/{user}"
    else:
        req_url = f"{fba_url}ds/nfl/assign/discord/{team_id}/{user}"
    res = requests.get(f"{req_url}")
    if res.status_code == 200:
        return True
    return False