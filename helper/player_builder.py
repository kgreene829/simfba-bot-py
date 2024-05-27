def GetPriorityFields(data):
    attrList = []
    if data['Position'] == "QB":
        sgr = ""
        if data['Shotgun'] == -1:
            sgr = "Under Center"
        elif data['Shotgun'] == 0:
            sgr = "Balanced"
        else:
            sgr = "Shotgun"
        attrList = [
        {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Carrying",
          "value": data['CarryingGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },
        {
          "name": "Throw Power",
          "value": data['ThrowPowerGrade'],
          "inline": True,
        },
        {
          "name": "Throw Accuracy",
          "value": data['ThrowAccuracyGrade'],
          "inline": True, 
        },
        {
          "name": "Shotgun Rating",
          "value": sgr,
          "inline": True, 
        }
        ]
    elif data['Position'] == "RB":
         attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Carrying",
          "value": data['CarryingGrade'],
          "inline": True,
        },   {
          "name": "Catching",
          "value": data['CatchingGrade'],
          "inline": True,
        },
        {
          "name": "Pass Block",
          "value": data['PassBlockGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "FB":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Carrying",
          "value": data['CarryingGrade'],
          "inline": True,
        },   {
          "name": "Catching",
          "value": data['CatchingGrade'],
          "inline": True,
        },
        {
          "name": "Pass Block",
          "value": data['PassBlockGrade'],
          "inline": True,
        },{
          "name": "Run Block",
          "value": data['RunBlockGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "WR":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Carrying",
          "value": data['CarryingGrade'],
          "inline": True,
        },   {
          "name": "Catching",
          "value": data['CatchingGrade'],
          "inline": True,
        },
        {
          "name": "Route Running",
          "value": data['RouteRunningGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "TE":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Carrying",
          "value": data['CarryingGrade'],
          "inline": True,
        },   
        {
          "name": "Catching",
          "value": data['CatchingGrade'],
          "inline": True,
        },
        {
          "name": "Route Running",
          "value": data['RouteRunningGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },        
        {
          "name": "Pass Block",
          "value": data['PassBlockGrade'],
          "inline": True,
        },
        {
          "name": "Run Block",
          "value": data['RunBlockGrade'],
          "inline": True,
        },
        ]
    elif data['Position'] == "OG" or data['Position'] == "OT" or data['Position'] == "C":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },        
        {
          "name": "Pass Block",
          "value": data['PassBlockGrade'],
          "inline": True,
        },
        {
          "name": "Run Block",
          "value": data['RunBlockGrade'],
          "inline": True,
        },
        ]
    elif data['Position'] == "DE":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Tackle",
          "value": data['TackleGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },        
        {
          "name": "Pass Rush",
          "value": data['PassRushGrade'],
          "inline": True,
        },
        {
          "name": "Run Defense",
          "value": data['RunDefenseGrade'],
          "inline": True,
        },
        ]
    elif data['Position'] == "DT":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Tackle",
          "value": data['TackleGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },        
        {
          "name": "Pass Rush",
          "value": data['PassRushGrade'],
          "inline": True,
        },
        {
          "name": "Run Defense",
          "value": data['RunDefenseGrade'],
          "inline": True,
        },
        ]
    elif data['Position'] == "ILB" or data['Position'] == "OLB":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Tackle",
          "value": data['TackleGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },        
        {
          "name": "Pass Rush",
          "value": data['PassRushGrade'],
          "inline": True,
        },
        {
          "name": "Run Defense",
          "value": data['RunDefenseGrade'],
          "inline": True,
        },
        {
          "name": "Zone Coverage",
          "value": data['ZoneCoverageGrade'],
          "inline": True,
        },
        {
          "name": "Man Coverage",
          "value": data['ManCoverageGrade'],
          "inline": True,
        },
        ]
    elif data['Position'] == "CB":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Tackle",
          "value": data['TackleGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },        
        {
          "name": "Zone Coverage",
          "value": data['ZoneCoverageGrade'],
          "inline": True,
        },
        {
          "name": "Man Coverage",
          "value": data['ManCoverageGrade'],
          "inline": True,
        },
        {
          "name": "Catching",
          "value": data['CatchingGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "FS" or data['Position'] == "SS":
        attrList = [
              {
          "name": "Agility",
          "value": data['AgilityGrade'],
          "inline": True,
        },
        {
          "name": "Speed",
          "value": data['SpeedGrade'],
          "inline": True,
        },
        {
          "name": "Tackle",
          "value": data['TackleGrade'],
          "inline": True,
        },
        {
          "name": "Strength",
          "value": data['StrengthGrade'],
          "inline": True,
        },
        {
          "name": "Run Defense",
          "value": data['RunDefenseGrade'],
          "inline": True,
        },       
        {
          "name": "Zone Coverage",
          "value": data['ZoneCoverageGrade'],
          "inline": True,
        },
        {
          "name": "Man Coverage",
          "value": data['ManCoverageGrade'],
          "inline": True,
        },
        {
          "name": "Catching",
          "value": data['CatchingGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "K":
        attrList = [
        {
          "name": "Kick Power",
          "value": data['KickPowerGrade'],
          "inline": True,
        },
        {
          "name": "Kick Accuracy",
          "value": data['KickAccuracyGrade'],
          "inline": True,
        }
        ]
    elif data['Position'] == "P":
        attrList = [
         {
          "name": "Punt Power",
          "value": data['PuntPowerGrade'],
          "inline": True,
        },
        {
          "name": "Punt Accuracy",
          "value": data['PuntAccuracyGrade'],
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
    attrList.append({
          "name": "Football IQ",
          "value": data['FootballIQGrade'],
          "inline": True,
        })
    attrList.append({
          "name": "Stamina",
          "value": data['StaminaGrade'],
          "inline": True,
        })
    attrList.append({
          "name": "Potential",
          "value": data['PotentialGrade'],
          "inline": True,
        })
    attrList.append({
          "name": "Injury",
          "value": data['InjuryGrade'],
          "inline": True,
        })
    if len(data['RedshirtStatus']) > 0:
        attrList.append({
          "name": "Redshirt Status",
          "value": data['RedshirtStatus'],
          "inline": True,
        })
    return attrList