from helper import util

def GetPriorityFields(data):
    attrList = []
    if data['Position'] == "C":
        attrList = [
        {
          "name": "Agility",
          "value": util.GetHockeyLetterGrade(data['Agility'],1),
          "inline": True,
        },
        {
          "name": "Faceoff",
          "value": util.GetHockeyLetterGrade(data['Faceoffs'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": util.GetHockeyLetterGrade(data['LongShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": util.GetHockeyLetterGrade(data['LongShotPower'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": util.GetHockeyLetterGrade(data['CloseShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": util.GetHockeyLetterGrade(data['CloseShotPower'],1),
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": util.GetHockeyLetterGrade(data['Passing'],1),
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": util.GetHockeyLetterGrade(data['PuckHandling'],1),
          "inline": True,
        },
        {
          "name": "Strength",
          "value": util.GetHockeyLetterGrade(data['Strength'],1),
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": util.GetHockeyLetterGrade(data['BodyChecking'],1),
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": util.GetHockeyLetterGrade(data['StickChecking'],1),
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": util.GetHockeyLetterGrade(data['ShotBlocking'],1),
          "inline": True,
        }
        ]
    elif data['Position'] == "F":
         attrList = [
        {
          "name": "Agility",
          "value": util.GetHockeyLetterGrade(data['Agility'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": util.GetHockeyLetterGrade(data['LongShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": util.GetHockeyLetterGrade(data['LongShotPower'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": util.GetHockeyLetterGrade(data['CloseShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": util.GetHockeyLetterGrade(data['CloseShotPower'],1),
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": util.GetHockeyLetterGrade(data['Passing'],1),
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": util.GetHockeyLetterGrade(data['PuckHandling'],1),
          "inline": True,
        },
        {
          "name": "Strength",
          "value": util.GetHockeyLetterGrade(data['Strength'],1),
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": util.GetHockeyLetterGrade(data['BodyChecking'],1),
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": util.GetHockeyLetterGrade(data['StickChecking'],1),
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": util.GetHockeyLetterGrade(data['ShotBlocking'],1),
          "inline": True,
        }
        ]
    elif data['Position'] == "D":
        attrList = [
        {
          "name": "Agility",
          "value": util.GetHockeyLetterGrade(data['Agility'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": util.GetHockeyLetterGrade(data['LongShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": util.GetHockeyLetterGrade(data['LongShotPower'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": util.GetHockeyLetterGrade(data['CloseShotAccuracy'],1),
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": util.GetHockeyLetterGrade(data['CloseShotPower'],1),
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": util.GetHockeyLetterGrade(data['Passing'],1),
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": util.GetHockeyLetterGrade(data['PuckHandling'],1),
          "inline": True,
        },
        {
          "name": "Strength",
          "value": util.GetHockeyLetterGrade(data['Strength'],1),
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": util.GetHockeyLetterGrade(data['BodyChecking'],1),
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": util.GetHockeyLetterGrade(data['StickChecking'],1),
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": util.GetHockeyLetterGrade(data['ShotBlocking'],1),
          "inline": True,
        }
        ]
    elif data['Position'] == "G":
        attrList = [
              {
          "name": "Agility",
          "value": util.GetHockeyLetterGrade(data['Agility'],1),
          "inline": True,
        },
                    {
          "name": "Strength",
          "value": util.GetHockeyLetterGrade(data['Strength'],1),
          "inline": True,
        },
        {
          "name": "Goalkeeping",
          "value": util.GetHockeyLetterGrade(data['Goalkeeping'],1),
          "inline": True,
        },
        {
          "name": "Goalie Vision",
          "value": util.GetHockeyLetterGrade(data['GoalieVision'],1),
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
