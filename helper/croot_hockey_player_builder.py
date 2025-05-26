def GetPriorityFields(data):
    attrList = []
    if data['Position'] == "C":
        attrList = [
        {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Faceoff",
          "value": data['FaceoffsGrade'],
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": data['LongShotAccuracyGrade'],
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": data['LongShotPowerGrade'],
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": data['CloseShotAccuracyGrade'],
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": data['CloseShotPowerGrade'],
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": data['PassingGrade'],
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": data['PuckHandlingGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": data['BodyCheckingGrade'],
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": data['StickCheckingGrade'],
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": data['ShotBlockingGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "F":
         attrList = [
        {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": data['LongShotAccuracyGrade'],
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": data['LongShotPowerGrade'],
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": data['CloseShotAccuracyGrade'],
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": data['CloseShotPowerGrade'],
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": data['PassingGrade'],
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": data['PuckHandlingGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": data['BodyCheckingGrade'],
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": data['StickCheckingGrade'],
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": data['ShotBlockingGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "D":
        attrList = [
        {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": data['LongShotAccuracyGrade'],
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": data['LongShotPowerGrade'],
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": data['CloseShotAccuracyGrade'],
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": data['CloseShotPowerGrade'],
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": data['PassingGrade'],
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": data['PuckHandlingGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": data['BodyCheckingGrade'],
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": data['StickCheckingGrade'],
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": data['ShotBlockingGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "G":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Goalkeeping",
          "value": data['GoalkeepingGrade'],
          "inline": True,
        },
        {
          "name": "Goalie Vision",
          "value": data['GoalieVisionGrade'],
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
          "value": data['OverallGrade'],
          "inline": True,
        })
    return attrList
