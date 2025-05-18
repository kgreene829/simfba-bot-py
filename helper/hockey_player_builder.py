def GetPriorityFields(data):
    attrList = []
    if data['Position'] == "C":
        attrList = [
        {
          "name": "Agility",
          "value": data['Agility'],
          "inline": True,
        },
        {
          "name": "Faceoff",
          "value": data['Faceoffs'],
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": data['LongShotAccuracy'],
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": data['LongShotPower'],
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": data['CloseShotAccuracy'],
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": data['CloseShotPower'],
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": data['Passing'],
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": data['PuckHandling'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['Strength'],
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": data['BodyChecking'],
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": data['StickChecking'],
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": data['ShotBlocking'],
          "inline": True,
        }
        ]
    elif data['Position'] == "F":
         attrList = [
        {
          "name": "Agility",
          "value": data['Agility'],
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": data['LongShotAccuracy'],
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": data['LongShotPower'],
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": data['CloseShotAccuracy'],
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": data['CloseShotPower'],
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": data['Passing'],
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": data['PuckHandling'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['Strength'],
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": data['BodyChecking'],
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": data['StickChecking'],
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": data['ShotBlocking'],
          "inline": True,
        }
        ]
    elif data['Position'] == "D":
        attrList = [
        {
          "name": "Agility",
          "value": data['Agility'],
          "inline": True,
        },
        {
          "name": "Long Shot Accuracy",
          "value": data['LongShotAccuracy'],
          "inline": True,
        },
        {
          "name": "Long Shot Power",
          "value": data['LongShotPower'],
          "inline": True,
        },
        {
          "name": "Close Shot Accuracy",
          "value": data['CloseShotAccuracy'],
          "inline": True,
        },
        {
          "name": "Close Shot Power",
          "value": data['CloseShotPower'],
          "inline": True, 
        },
        {
          "name": "Passing",
          "value": data['Passing'],
          "inline": True,
        },
        {
          "name": "Puck Handling",
          "value": data['PuckHandling'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['Strength'],
          "inline": True,
        },
        {
          "name": "Body Checking",
          "value": data['BodyChecking'],
          "inline": True,
        },
        {
          "name": "Stick Checking",
          "value": data['StickChecking'],
          "inline": True,
        },
        {
          "name": "Shot Blocking",
          "value": data['ShotBlocking'],
          "inline": True,
        }
        ]
    elif data['Position'] == "G":
        attrList = [
              {
          "name": "Agility",
          "value": data['Agility'],
          "inline": True,
        {
          "name": "Goalkeeping",
          "value": data['Goalkeeping'],
          "inline": True,
        },
        {
          "name": "Goalie Vision",
          "value": data['GoalieVision'],
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
    return attrList
