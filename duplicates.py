import api_requests
from collections import defaultdict

games = api_requests.GetAllCBBMatches()
college_matches = games["CBBGames"]
matches_dict = defaultdict(int)
duplicates = []

for g in college_matches:
    team1, team2 = g["HomeTeam"], g["AwayTeam"]
    is_conference = g["IsConference"]
    if is_conference == False:
        match_key = tuple(sorted([team1, team2]))
        matches_dict[match_key] += 1
        if matches_dict[match_key] > 1:
            duplicates.append(g)

if duplicates:
    print("Found Duplicate Matches:")
    for dup in duplicates:
        print(dup)
else:
    print("No duplicates found")