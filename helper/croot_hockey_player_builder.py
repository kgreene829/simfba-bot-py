from util import GetHockeyLetterGrade

def GetPriorityFields(data):
    attrList = []
    if data['Position'] == "C":
        attrList = [
        {
          "name": "Agility",
          "value": GetHockeyLetterGrade(data['Agility'],1),
          "inline": True,
        },
        {
          "name": "Faceoff",
          "value": GetHockeyLetterGrade(data['Faceoffs'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": GetHockeyLetterGrade(data['LongShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": GetHockeyLetterGrade(data['LongShotPower'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": GetHockeyLetterGrade(data['CloseShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": GetHockeyLetterGrade(data['CloseShotPower'],1),
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": GetHockeyLetterGrade(data['Passing'],1),
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": GetHockeyLetterGrade(data['PuckHandling'],1),
          "inline": True,
        },
        {
          "name": "Strength",
          "value": GetHockeyLetterGrade(data['Strength'],1),
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": GetHockeyLetterGrade(data['BodyChecking'],1),
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": GetHockeyLetterGrade(data['StickChecking'],1),
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": GetHockeyLetterGrade(data['ShotBlocking'],1),
          "inline": True,
        }
        ]
    elif data['Position'] == "F":
         attrList = [
        {
          "name": "Agility",
          "value": GetHockeyLetterGrade(data['Agility'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": GetHockeyLetterGrade(data['LongShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": GetHockeyLetterGrade(data['LongShotPower'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": GetHockeyLetterGrade(data['CloseShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": GetHockeyLetterGrade(data['CloseShotPower'],1),
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": GetHockeyLetterGrade(data['Passing'],1),
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": GetHockeyLetterGrade(data['PuckHandling'],1),
          "inline": True,
        },
        {
          "name": "Strength",
          "value": GetHockeyLetterGrade(data['Strength'],1),
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": GetHockeyLetterGrade(data['BodyChecking'],1),
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": GetHockeyLetterGrade(data['StickChecking'],1),
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": GetHockeyLetterGrade(data['ShotBlocking'],1),
          "inline": True,
        }
        ]
    elif data['Position'] == "D":
        attrList = [
        {
          "name": "Agility",
          "value": GetHockeyLetterGrade(data['Agility'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": GetHockeyLetterGrade(data['LongShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": GetHockeyLetterGrade(data['LongShotPower'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": GetHockeyLetterGrade(data['CloseShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": GetHockeyLetterGrade(data['CloseShotPower'],1),
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": GetHockeyLetterGrade(data['Passing'],1),
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": GetHockeyLetterGrade(data['PuckHandling'],1),
          "inline": True,
        },
        {
          "name": "Strength",
          "value": GetHockeyLetterGrade(data['Strength'],1),
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": GetHockeyLetterGrade(data['BodyChecking'],1),
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": GetHockeyLetterGrade(data['StickChecking'],1),
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": GetHockeyLetterGrade(data['ShotBlocking'],1),
          "inline": True,
        }
        ]
    elif data['Position'] == "G":
        attrList = [
              {
          "name": "Agility",
          "value": GetHockeyLetterGrade(data['Agility'],1),
          "inline": True,
        },
                    {
          "name": "Strength",
          "value": GetHockeyLetterGrade(data['Strength'],1),
          "inline": True,
        },
        {
          "name": "Goalkeeping",
          "value": GetHockeyLetterGrade(data['Goalkeeping'],1),
          "inline": True,
        },
        {
          "name": "Goalie Vision",
          "value": GetHockeyLetterGrade(data['GoalieVision'],1),
          "inline": True,
        }
        ]
    attrList.insert(0, {
          "name": "Stars",
          "value": data['Stars'],
          "inline": False,
        })
    attrList.insert(0, {
          "name": "Overall",
          "value": data['Overall'],
          "inline": True,
        })
    attrList.append({
          "name": "Stamina",
          "value": data['Stamina'],
          "inline": True,
        })
    attrList.append({
          "name": "Injury",
          "value": data['InjuryRating'],
          "inline": True,
        })
    return attrList
