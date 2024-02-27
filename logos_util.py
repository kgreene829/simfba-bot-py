import logos

def GetLogo(team):
  match team:
    case "USAF":
      return logos.logo_book["Air_Force"]
    case "AAMU":
      return logos.logo_book["Alabama_AM"]
    case "ACU":
      return logos.logo_book["Abilene_Christian"]
    case "AKRN":
      return logos.logo_book["Akron_Zips"]
    case "ALB":
      return logos.logo_book["Albany"]
    case "ALCN":
      return logos.logo_book["Alcorn_State"]
    case "ALST":
      return logos.logo_book["Alabama_State"]
    case "AMCC":
      return logos.logo_book["Texas_AM_Corpus"]
    case "AMER":
      return logos.logo_book["American"]
    case "APSU":
      return logos.logo_book["Austin_Peay"]
    case "BAMA":
      return logos.logo_book["Alabama"]
    case "APST":
      return logos.logo_book["App_State"]
    case "ZONA":
      return logos.logo_book["Arizona"]
    case "AZST":
      return logos.logo_book["Arizona_State"]
    case "ARK":
      return logos.logo_book["Arkansas"]
    case "ARST":
      return logos.logo_book["Arkansas_State"]
    case "ARMY":
      return logos.logo_book["Army"]
    case "AUB":
      return logos.logo_book["Auburn"]
    case "BALL":
      return logos.logo_book["Ball_State"]
    case "BAYL":
      return logos.logo_book["Baylor"]
    case "BOIS":
      return logos.logo_book["Boise_State"]
    case "BC":
      return logos.logo_book["Boston_College"]
    case "BCU":
      return logos.logo_book["Bethune_Cookman"]
    case "BEL":
      return logos.logo_book["Belmont"]
    case "BELL":
      return logos.logo_book["Bellarmine"]
    case "BGSU":
      return logos.logo_book["Bowling_Green"]
    case "BING":
      return logos.logo_book["Binghamton"]
    case "BRAD":
      return logos.logo_book["Bradley"]
    case "BRWN":
      return logos.logo_book["Brown"]
    case "BRY":
      return logos.logo_book["Bryant"]
    case "BU":
      return logos.logo_book["Boston"]
    case "BUFF":
      return logos.logo_book["Buffalo"]
    case "BUCK":
      return logos.logo_book["Bucknell"]
    case "BUT":
      return logos.logo_book["Butler"]
    case "BYU":
      return logos.logo_book["BYU"]
    case "CAL":
      return logos.logo_book["California"]
    case "CAMP":
      return logos.logo_book["Campbell"]
    case "CAN":
      return logos.logo_book["Canisius"]
    case "CARK":
      return logos.logo_book["Central_Arkansas"]
    case "CBU":
      return logos.logo_book["California_Baptist"]
    case "CCSU":
      return logos.logo_book["Central_Connecticut"]
    case "CMU":
      return logos.logo_book["Central_Michigan"]
    case "CHAM":
      return logos.logo_book["Chaminade"]
    case "CHSO":
      return logos.logo_book["Charleston_Southern"]
    case "CHST":
      return logos.logo_book["Chicago_State"]
    case "CHAR":
      return logos.logo_book["Charlotte"]
    case "CINC":
      return logos.logo_book["Cincinnati"]
    case "CIT":
      return logos.logo_book["Citadel"]
    case "CLEM":
      return logos.logo_book["Clemson"]
    case "CLEV":
      return logos.logo_book["Cleveland_State"]
    case "CCU":
      return logos.logo_book["Coastal_Carolina"]
    case "COFC":
      return logos.logo_book["Charleston"]
    case "COLG":
      return logos.logo_book["Colgate"]
    case "COLO":
      return logos.logo_book["Colorado"]
    case "COLU":
      return logos.logo_book["Columbia"]
    case "COPP":
      return logos.logo_book["Coppin_State"]
    case "COR":
      return logos.logo_book["Cornell"]
    case "CP":
      return logos.logo_book["Cal_Poly"]
    case "CSUB":
      return logos.logo_book["Cal_State_Bakersfield"]
    case "CSUF":
      return logos.logo_book["Cal_State_Fullerton"]
    case "CSUN":
      return logos.logo_book["Cal_State_Northridge"]
    case "CSU":
      return logos.logo_book["Colorado_State"]
    case "CREI":
      return logos.logo_book["Creighton"]
    case "DART":
      return logos.logo_book["Dartmouth"]
    case "DAV":
      return logos.logo_book["Davidson"]
    case "DAY":
      return logos.logo_book["Dayton"]
    case "DEL":
      return logos.logo_book["Delaware"]
    case "DETM":
      return logos.logo_book["Detroit_Mercy"]
    case "DREX":
      return logos.logo_book["Drexel"]
    case "DRKE":
      return logos.logo_book["Drake"]
    case "DSU":
      return logos.logo_book["Delaware_State"]
    case "DU":
      return logos.logo_book["Denver"]
    case "DUKE":
      return logos.logo_book["Duke"]
    case "DUQ":
      return logos.logo_book["Duquesne"]
    case "ECU":
      return logos.logo_book["East_Carolina"]
    case "EIU":
      return logos.logo_book["Eastern_Illinois"]
    case "EKU":
      return logos.logo_book["Eastern_Kentucky"]
    case "ELON":
      return logos.logo_book["Elon"]
    case "EMU":
      return logos.logo_book["Eastern_Michigan"]
    case "ETSU":
      return logos.logo_book["ETSU"]
    case "EWU":
      return logos.logo_book["Eastern_Washington"]
    case "FAIR":
      return logos.logo_book["Fairfield"]
    case "FAMU":
      return logos.logo_book["FAMU"]
    case "FDU":
      return logos.logo_book["Fairleigh_Dickinson"]
    case "FIU":
      return logos.logo_book["FIU"]
    case "FLA":
      return logos.logo_book["Florida"]
    case "FAU":
      return logos.logo_book["Florida_Atlantic"]
    case "FSU":
      return logos.logo_book["Florida_State"]
    case "FOR":
      return logos.logo_book["Fordham"]
    case "FRES":
      return logos.logo_book["Fresno_State"]
    case "FUR":
      return logos.logo_book["Furman"]
    case "GCU":
      return logos.logo_book["Grand_Canyon"]
    case "GMU":
      return logos.logo_book["GeorgeMason"]
    case "GRAM":
      return logos.logo_book["Grambling_State"]
    case "GW":
      return logos.logo_book["GeorgeWashington"]
    case "UGA":
      return logos.logo_book["Georgia"]
    case "GASO":
      return logos.logo_book["Georgia_Southern"]
    case "GAST":
      return logos.logo_book["Georgia_State"]
    case "GT":
      return logos.logo_book["Georgia_Tech"]
    case "GONZ":
      return logos.logo_book["Gonzaga"]
    case "HAMP":
      return logos.logo_book["Hampton"]
    case "HART":
      return logos.logo_book["Hartford"]
    case "HARV":
      return logos.logo_book["Harvard"]
    case "HAWI":
      return logos.logo_book["Hawaii"]
    case "HC":
      return logos.logo_book["Holy_Cross"]
    case "UHOU":
      return logos.logo_book["Houston"]
    case "HCU":
      return logos.logo_book["Houston_Baptist"]
    case "HOF":
      return logos.logo_book["Hofstra"]
    case "HOW":
      return logos.logo_book["Howard"]
    case "HP":
      return logos.logo_book["High_Point"]
    case "IDHO":
      return logos.logo_book["Idaho"]
    case "IDST":
      return logos.logo_book["Idaho_State"]
    case "ILLI":
      return logos.logo_book["Illinois"]
    case "ILST":
      return logos.logo_book["Illinois_State"]
    case "IND":
      return logos.logo_book["Indiana"]
    case "INST":
      return logos.logo_book["Indiana_State"]
    case "IONA":
      return logos.logo_book["Iona"]
    case "IOWA":
      return logos.logo_book["Iowa"]
    case "IAST":
      return logos.logo_book["Iowa_State"]
    case "IUPU":
      return logos.logo_book["IUPUI"]
    case "JMU":
      return logos.logo_book["JMU"]
    case "JXST":
      return logos.logo_book["Jackson_State"]
    case "JST":
      return logos.logo_book["JacksonvilleState"]
    case "KANS":
      return logos.logo_book["Kansas"]
    case "KCU":
      return logos.logo_book["Kansas_City_U"]
    case "KSST":
      return logos.logo_book["Kansas_State"]
    case "KENT":
      return logos.logo_book["Kent_State"]
    case "KNSW":
      return logos.logo_book["KennesawState"]
    case "UKEN":
      return logos.logo_book["Kentucky"]
    case "LAS":
      return logos.logo_book["LaSalle"]
    case "LAF":
      return logos.logo_book["Lafayette"]
    case "LAM":
      return logos.logo_book["Lamar"]
    case "LBSU":
      return logos.logo_book["Long_Beach"]
    case "LEH":
      return logos.logo_book["LeHigh"]
    case "LEM":
      return logos.logo_book["Lemoyne"]
    case "LIN":
      return logos.logo_book["Lindenwood"]
    case "LIP":
      return logos.logo_book["Lipscomb"]
    case "LIU":
      return logos.logo_book["Long_Island"]
    case "L-MD":
      return logos.logo_book["Loyola_Maryland"]
    case "LONG":
      return logos.logo_book["Longwood"]
    case "LR":
      return logos.logo_book["Little_Rock"]
    case "LU":
      return logos.logo_book["Liberty"]
    case "ULL":
      return logos.logo_book["Louisiana"]
    case "ULM":
      return logos.logo_book["Louisiana_Monroe"]
    case "LT":
      return logos.logo_book["Louisiana_Tech"]
    case "LOU":
      return logos.logo_book["Louisville"]
    case "LUC":
      return logos.logo_book["LoyolaC"]
    case "LMU":
      return logos.logo_book["LoyolaM"]
    case "LSU":
      return logos.logo_book["LSU"]
    case "MAN":
      return logos.logo_book["Manhattan"]
    case "MCN":
      return logos.logo_book["McNeese_State"]
    case "MARQ":
      return logos.logo_book["Marquette"]
    case "ME":
      return logos.logo_book["Maine"]
    case "MRSH":
      return logos.logo_book["Marshall"]
    case "UMD":
      return logos.logo_book["Maryland"]
    case "MEMP":
      return logos.logo_book["Memphis"]
    case "MER":
      return logos.logo_book["Mercer"]
    case "MIAF":
      return logos.logo_book["Miami"]
    case "MIAO":
      return logos.logo_book["Miami_OH"]
    case "MICH":
      return logos.logo_book["Michigan"]
    case "MIST":
      return logos.logo_book["Michigan_State"]
    case "MILW":
      return logos.logo_book["Milwaukee"]
    case "MTSU":
      return logos.logo_book["Middle_Tennessee"]
    case "MINN":
      return logos.logo_book["Minnesota"]
    case "MSST":
      return logos.logo_book["Mississippi_State"]
    case "MIZZ":
      return logos.logo_book["Missouri"]
    case "MONM":
      return logos.logo_book["Monmouth"]
    case "MONT":
      return logos.logo_book["Montana"]
    case "MORE":
      return logos.logo_book["Morehead"]
    case "MORG":
      return logos.logo_book["Morgan_State"]
    case "MOST":
      return logos.logo_book["Missouri_State"]
    case "MRMK":
      return logos.logo_book["Merrimack"]
    case "MRST":
      return logos.logo_book["Marist"]
    case "MSM":
      return logos.logo_book["Mount_St_Marys"]
    case "MSVU":
      return logos.logo_book["Mississippi_Valley"]
    case "MTST":
      return logos.logo_book["Montana_State"]
    case "MUR":
      return logos.logo_book["Murray_State"]
    case "NAU":
      return logos.logo_book["Northern_Arizona"]
    case "NAVY":
      return logos.logo_book["Navy"]
    case "NCAT":
      return logos.logo_book["North_Carolina_AT"]
    case "NCCU":
      return logos.logo_book["North_Carolina_Central"]
    case "NCST":
      return logos.logo_book["NC_State"]
    case "NDSU":
      return logos.logo_book["North_Dakota_State"]
    case "NE":
      return logos.logo_book["Northeastern"]
    case "NEB":
      return logos.logo_book["Nebraska"]
    case "NEV":
      return logos.logo_book["Nevada"]
    case "NIA":
      return logos.logo_book["Niagara"]
    case "NICH":
      return logos.logo_book["Nicholls_State"]
    case "NJIT":
      return logos.logo_book["NJIT"]
    case "NKU":
      return logos.logo_book["Northern_Kentucky"]
    case "UNM":
      return logos.logo_book["New_Mexico"]
    case "NMSU":
      return logos.logo_book["New_Mexico_State"]
    case "UNC":
      return logos.logo_book["North_Carolina"]
    case "UNT":
      return logos.logo_book["North_Texas"]
    case "NIU":
      return logos.logo_book["NIU"]
    case "NORF":
      return logos.logo_book["Norfolk_State"]
    case "NW":
      return logos.logo_book["Northwestern"]
    case "NWST":
      return logos.logo_book["Northwestern_State"]
    case "ND":
      return logos.logo_book["Notre_Dame"]
    case "OAK":
      return logos.logo_book["Oakland"]
    case "OHIO":
      return logos.logo_book["Ohio"]
    case "OHST":
      return logos.logo_book["Ohio_State"]
    case "OKLA":
      return logos.logo_book["Oklahoma"]
    case "OKST":
      return logos.logo_book["Oklahoma_State"]
    case "ODU":
      return logos.logo_book["Old_Dominion"]
    case "MISS":
      return logos.logo_book["Ole_Miss"]
    case "OREG":
      return logos.logo_book["Oregon"]
    case "ORST":
      return logos.logo_book["Oregon_State"]
    case "ORU":
      return logos.logo_book["Oral_Roberts"]
    case "PAC":
      return logos.logo_book["Pacific"]
    case "PENN":
      return logos.logo_book["Pennsylvania"]
    case "PFW":
      return logos.logo_book["Purdue_Fort_Wayne"]
    case "PRE":
      return logos.logo_book["Presbyterian_College"]
    case "PNST":
      return logos.logo_book["Penn_State"]
    case "PEPP":
      return logos.logo_book["Pepperdine"]
    case "PITT":
      return logos.logo_book["Pitt"]
    case "PRIN":
      return logos.logo_book["Princeton"]
    case "PROV":
      return logos.logo_book["Providence"]
    case "PRST":
      return logos.logo_book["Portland_State"]
    case "PURD":
      return logos.logo_book["Purdue"]
    case "PV":
      return logos.logo_book["Prairie_View"]
    case "QUIN":
      return logos.logo_book["Quinnipiac"]
    case "QUOC":
      return logos.logo_book["Queens"]
    case "RAD":
      return logos.logo_book["Radford"]
    case "RGV":
      return logos.logo_book["Rio_Grande_Valley"]
    case "RID":
      return logos.logo_book["Rider"]
    case "RMU":
      return logos.logo_book["Robert_Morris"]
    case "URI":
      return logos.logo_book["RhodeIsland"]
    case "RICE":
      return logos.logo_book["Rice"]
    case "RICH":
      return logos.logo_book["Richmond"]
    case "RUTG":
      return logos.logo_book["Rutgers"]
    case "JOES":
      return logos.logo_book["SaintJosephs"]
    case "SLU":
      return logos.logo_book["SaintLouis"]
    case "SAM":
      return logos.logo_book["Samford"]
    case "SCST":
      return logos.logo_book["South_Carolina_State"]
    case "SDAK":
      return logos.logo_book["South_Dakota"]
    case "SDSU":
      return logos.logo_book["San_Diego_State"]
    case "SELA":
      return logos.logo_book["Southeastern_Louisiana"]
    case "SEMO":
      return logos.logo_book["Southeast_Missouri"]
    case "SF":
      return logos.logo_book["SFDons"]
    case "SFA":
      return logos.logo_book["SFA"]
    case "SFNY":
      return logos.logo_book["St_Francis"]
    case "SFPA":
      return logos.logo_book["Saint_Francis"]
    case "SHSU":
      return logos.logo_book["SamHoustonState"]
    case "SHU":
      return logos.logo_book["Sacred_Heart"]
    case "SIE":
      return logos.logo_book["Siena"]
    case "SIU":
      return logos.logo_book["Southern_Illinois"]
    case "SIUE":
      return logos.logo_book["SIU_E"]
    case "SJSU":
      return logos.logo_book["San_Jose"]
    case "SCU":
      return logos.logo_book["SantaClara"]
    case "HALL":
      return logos.logo_book["SetonHall"]
    case "SMU":
      return logos.logo_book["SMU"]
    case "SOU":
      return logos.logo_book["Southern"]
    case "SPU":
      return logos.logo_book["Saint_Peters"]
    case "USA":
      return logos.logo_book["South_Alabama"]
    case "SOCA":
      return logos.logo_book["South_Carolina"]
    case "SSU":
      return logos.logo_book["Sacramento_State"]
    case "USF":
      return logos.logo_book["South_Florida"]
    case "USM":
      return logos.logo_book["Southern_Miss"]
    case "SJU":
      return logos.logo_book["StJohns"]
    case "STAN":
      return logos.logo_book["Stanford"]
    case "STBK":
      return logos.logo_book["Stony_Brook"]
    case "STET":
      return logos.logo_book["Stetson"]
    case "STMN":
      return logos.logo_book["St_Thomas"]
    case "STO":
      return logos.logo_book["Stonehill"]
    case "SUU":
      return logos.logo_book["Southern_Utah"]
    case "CUSE":
      return logos.logo_book["Syracuse"]
    case "TAMC":
      return logos.logo_book["Texas_AM_Commerce"]
    case "TAR":
      return logos.logo_book["Tarleton"]
    case "TCU":
      return logos.logo_book["TCU"]
    case "TEMP":
      return logos.logo_book["Temple"]
    case "TENN":
      return logos.logo_book["Tennessee"]
    case "TNST":
      return logos.logo_book["Tennessee_State"]
    case "TNTC":
      return logos.logo_book["Tennessee_Tech"]
    case "TEX":
      return logos.logo_book["Texas"]
    case "TAMU":
      return logos.logo_book["TAMU"]
    case "TXST":
      return logos.logo_book["Texas_State"]
    case "TTU":
      return logos.logo_book["Texas_Tech"]
    case "TXSO":
      return logos.logo_book["Texas_Southern"]
    case "TLDO":
      return logos.logo_book["Toledo"]
    case "TOW":
      return logos.logo_book["Towson"]
    case "TROY":
      return logos.logo_book["Troy"]
    case "TLNE":
      return logos.logo_book["Tulane"]
    case "TULS":
      return logos.logo_book["Tulsa"]
    case "UAB":
      return logos.logo_book["UAB"]
    case "UAPB":
      return logos.logo_book["Arkansas_Pine_Bluff"]
    case "UCD":
      return logos.logo_book["UC_Davis"]
    case "UCR":
      return logos.logo_book["UC_Riverside"]
    case "UCSB":
      return logos.logo_book["UC_Santa_Barbara"]
    case "UIC":
      return logos.logo_book["UIC"]
    case "UIW":
      return logos.logo_book["Incarnate_Word"]
    case "UCF":
      return logos.logo_book["UCF"]
    case "UCLA":
      return logos.logo_book["UCLA"]
    case "CONN":
      return logos.logo_book["Connecticut"]
    case "MASS":
      return logos.logo_book["UMASS"]
    case "UMES":
      return logos.logo_book["Maryland_East"]
    case "UML":
      return logos.logo_book["UMASS_Lowell"]
    case "UNA":
      return logos.logo_book["North_Alabama"]
    case "UNCA":
      return logos.logo_book["UNC_Asheville"]
    case "UNCO":
      return logos.logo_book["Northern_Colorado"]
    case "UNCG":
      return logos.logo_book["UNCG"]
    case "UNCW":
      return logos.logo_book["UNC_Wilmington"]
    case "UND":
      return logos.logo_book["North_Dakota"]
    case "UNF":
      return logos.logo_book["North_Florida"]
    case "UNH":
      return logos.logo_book["New_Hampshire"]
    case "UNI":
      return logos.logo_book["Northern_Iowa"]
    case "UNO":
      return logos.logo_book["New_Orleans"]
    case "UOG":
      return logos.logo_book["Guam"]
    case "UNLV":
      return logos.logo_book["UNLV"]
    case "UPST":
      return logos.logo_book["USC_Upstate"]
    case "USC":
      return logos.logo_book["USC"]
    case "USI":
      return logos.logo_book["Southern_Indiana"]
    case "UTA":
      return logos.logo_book["UT_Arlington"]
    case "UTC":
      return logos.logo_book["Chattanooga"]
    case "UTM":
      return logos.logo_book["UT_Martin"]
    case "UTU":
      return logos.logo_book["Utah_Tech"]
    case "UTEP":
      return logos.logo_book["UTEP"]
    case "UTSA":
      return logos.logo_book["UTSA"]
    case "UTAH":
      return logos.logo_book["Utah"]
    case "UTST":
      return logos.logo_book["Utah_State"]
    case "UV":
      return logos.logo_book["Vermont"]
    case "UVU":
      return logos.logo_book["Utah_Valley"]
    case "UWGB":
      return logos.logo_book["Green_Bay"]
    case "VAL":
      return logos.logo_book["Valparaiso"]
    case "VAND":
      return logos.logo_book["Vanderbilt"]
    case "VILL":
      return logos.logo_book["Villanova"]
    case "UVA":
      return logos.logo_book["Virginia"]
    case "VMI":
      return logos.logo_book["VMI"]
    case "VT":
      return logos.logo_book["Virginia_Tech"]
    case "WAG":
      return logos.logo_book["Wagner"]
    case "WAKE":
      return logos.logo_book["Wake_Forest"]
    case "WASH":
      return logos.logo_book["Washington"]
    case "WAST":
      return logos.logo_book["Washington_State"]
    case "WCU":
      return logos.logo_book["Western_Carolina"]
    case "WEB":
      return logos.logo_book["Weber_State"]
    case "WEBB":
      return logos.logo_book["Gardner_Webb"]
    case "WIN":
      return logos.logo_book["Winthrop"]
    case "WIU":
      return logos.logo_book["Western_Illinois"]
    case "W&M":
      return logos.logo_book["William_and_Mary"]
    case "WOF":
      return logos.logo_book["Wofford"]
    case "WRST":
      return logos.logo_book["Wright_State"]
    case "WVU":
      return logos.logo_book["West_Virginia"]
    case "WKU":
      return logos.logo_book["Western_Kentucky"]
    case "WMU":
      return logos.logo_book["Western_Michigan"]
    case "WISC":
      return logos.logo_book["Wisconsin"]
    case "WYOM":
      return logos.logo_book["Wyoming"]
    case "XAV":
      return logos.logo_book["Xavier"]
    case "YALE":
      return logos.logo_book["Yale"]
    case "YSU":
      return logos.logo_book["Youngstown_State"]
    case "UMBC":
      return logos.logo_book["UMBC"]
    case "WICH":
      return logos.logo_book["Wichita_State"]
    case "USD":
      return logos.logo_book["U_San_Diego"]
    case "UCSD":
      return logos.logo_book["UC_San_Diego"]
    case "SMC":
      return logos.logo_book["St_Marys"]
    case "VCU":
      return logos.logo_book["VCU"]
    case "GEOT":
      return logos.logo_book["Georgetown"]
    case "SBON":
      return logos.logo_book["St_Bonaventure"]
    case "UCI":
      return logos.logo_book["UC_Irvine"]
    case "SDST":
      return logos.logo_book["South_Dakota_State"]
    case "DPU":
      return logos.logo_book["DePaul"]
    case "FGCU":
      return logos.logo_book["FGCU"]
    case "JU":
      return logos.logo_book["Jacksonville"]
    case "UNOM":
      return logos.logo_book["Nebraska_Omaha"]
    case "PORT":
      return logos.logo_book["Portland"]
    case "SEAU":
      return logos.logo_book["Seattle"]
    case "EVAN":
      return logos.logo_book["Evansville"]
    case "Arizona Cardinals":
      return logos.logo_book["ARI_Cardinals"]
    case "Atlanta Falcons":
      return logos.logo_book["ATL_Falcons"]
    case "Baltimore Ravens":
      return logos.logo_book["BAL_Ravens"]
    case "Buffalo Bills":
      return logos.logo_book["BUF_Bills"]
    case "Carolina Panthers":
      return logos.logo_book["CAR_Panthers"]
    case "Cincinnati Bengals":
      return logos.logo_book["CIN_Bengals"]
    case "Cleveland Browns":
      return logos.logo_book["CLE_Browns"]
    case "Chicago Bears":
      return logos.logo_book["CHI_Bears"]
    case "Dallas Cowboys":
      return logos.logo_book["DAL_Cowboys"]
    case "Denver Broncos":
      return logos.logo_book["DEN_Broncos"]
    case "Detroit Lions":
      return logos.logo_book["DET_Lions"]
    case "Green Bay Packers":
      return logos.logo_book["GB_Packers"]
    case "Houston Texans":
      return logos.logo_book["HOU_Texans"]
    case "Indiana Pacers":
      return logos.logo_book["IND_Pacers"]
    case "Indianapolis Colts":
      return logos.logo_book["IND_Colts"]
    case "Jacksonville Jaguars":
      return logos.logo_book["JAX_Jaguars"]
    case "Kansas City Chiefs":
      return logos.logo_book["KC_Chiefs"]
    case "Las Vegas Raiders":
      return logos.logo_book["LV_Raiders"]
    case "Los Angeles Rams":
      return logos.logo_book["LA_Rams"]
    case "Los Angeles Chargers":
      return logos.logo_book["LA_Chargers"]
    case "Miami Dolphins":
      return logos.logo_book["MIA_Dolphins"]
    case "Minnesota Vikings":
      return logos.logo_book["MN_Vikings"]
    case "New England Patriots":
      return logos.logo_book["NE_Patriots"]
    case "New Orleans Saints":
      return logos.logo_book["NO_Saints"]

    case "New York Giants":
      return logos.logo_book["NY_Giants"]
    case "New York Jets":
      return logos.logo_book["NY_Jets"]
    case "Philadelphia Eagles":
      return logos.logo_book["PHI_Eagles"]
    case "Pittsburgh Steelers":
      return logos.logo_book["PIT_Steelers"]
    case "San Francisco 49ers":
      return logos.logo_book["SF_49ers"]
    case "Seattle Seahawks":
      return logos.logo_book["SEA_Seahawks"]
    case "Tampa Bay Buccaneers":
      return logos.logo_book["TB_Buccaneers"]
    case "Tennessee Titans":
      return logos.logo_book["TEN_Titans"]
    case "Washington Commanders":
      return logos.logo_book["WAS_Commies"]

    case _:
      return logos.logo_book["Unknown"]
    
def GetNBALogo(team):
  match (team):
    case "ATL":
      return logos.logo_book["ATL_Hawks"]
    case "Atlanta Hawks":
      return logos.logo_book["ATL_Hawks"]
    case "Atlanta":
      return logos.logo_book["ATL_Hawks"]
    case "BKN":
      return logos.logo_book["BRK_Nets"]
    case "Brooklyn":
      return logos.logo_book["BRK_Nets"]
    case "Brooklyn Nets":
      return logos.logo_book["BRK_Nets"]
    case "Boston":
      return logos.logo_book["BOS_Celtics"]
    case "BOS":
      return logos.logo_book["BOS_Celtics"]
    case "Boston Celtics":
      return logos.logo_book["BOS_Celtics"]
    case "CHA":
      return logos.logo_book["CHA_Hornets"]
    case "Charlotte":
      return logos.logo_book["CHA_Hornets"]
    case "Charlotte Hornets":
      return logos.logo_book["CHA_Hornets"]
    case "CHI":
      return logos.logo_book["CHI_Bulls"]
    case "Chicago":
      return logos.logo_book["CHI_Bulls"]
    case "Chicago Bulls":
      return logos.logo_book["CHI_Bulls"]
    case "CLE":
      return logos.logo_book["CLE_Cavaliers"]
    case "Cleveland":
      return logos.logo_book["CLE_Cavaliers"]
    case "Cleveland Cavaliers":
      return logos.logo_book["CLE_Cavaliers"]
    case "DAL":
      return logos.logo_book["DAL_Mavericks"]
    case "Dallas":
      return logos.logo_book["DAL_Mavericks"]
    case "Dallas Mavericks":
      return logos.logo_book["DAL_Mavericks"]
    case "DEN":
      return logos.logo_book["DEN_Nuggets"]
    case "Denver":
      return logos.logo_book["DEN_Nuggets"]
    case "Denver Nuggets":
      return logos.logo_book["DEN_Nuggets"]
    case "DET":
      return logos.logo_book["DET_Pistons"]
    case "Detroit":
      return logos.logo_book["DET_Pistons"]
    case "Detroit Pistons":
      return logos.logo_book["DET_Pistons"]
    case "GSW":
      return logos.logo_book["GS_Warriors"]
    case "Golden State":
      return logos.logo_book["GS_Warriors"]
    case "Golden State Warriors":
      return logos.logo_book["GS_Warriors"]
    case "HOU":
      return logos.logo_book["HOU_Rockets"]
    case "Houston":
      return logos.logo_book["HOU_Rockets"]
    case "Houston Rockets":
      return logos.logo_book["HOU_Rockets"]
    case "IND":
      return logos.logo_book["IND_Pacers"]
    case "Indiana":
      return logos.logo_book["IND_Pacers"]
    case "Indiana Pacers":
      return logos.logo_book["IND_Pacers"]
    case "LAL":
      return logos.logo_book["LA_Lakers"]
    case "Los Angeles":
      return logos.logo_book["LA_Lakers"]
    case "Los Angeles Lakers":
      return logos.logo_book["LA_Lakers"]
    case "SDC":
      return logos.logo_book["SD_Clippers"]
    case "San Diego":
      return logos.logo_book["SD_Clippers"]
    case "San Diego Clippers":
      return logos.logo_book["SD_Clippers"]
    case "MEM":
      return logos.logo_book["MEM_Grizzlies"]
    case "Memphis":
      return logos.logo_book["MEM_Grizzlies"]
    case "Memphis Grizzlies":
      return logos.logo_book["MEM_Grizzlies"]
    case "MIA":
      return logos.logo_book["MIA_Heat"]
    case "Miami":
      return logos.logo_book["MIA_Heat"]
    case "Miami Heat":
      return logos.logo_book["MIA_Heat"]
    case "MIL":
      return logos.logo_book["MIL_Bucks"]
    case "Milwaukee":
      return logos.logo_book["MIL_Bucks"]
    case "Milwaukee Bucks":
      return logos.logo_book["MIL_Bucks"]
    case "MIN":
      return logos.logo_book["MIN_Timberwolves"]
    case "Minnesota":
      return logos.logo_book["MIN_Timberwolves"]
    case "Minnesota Timberwolves":
      return logos.logo_book["MIN_Timberwolves"]
    case "NOP":
      return logos.logo_book["NO_Pelicans"]
    case "New Orleans":
      return logos.logo_book["NO_Pelicans"]
    case "New Orleans Pelicans":
      return logos.logo_book["NO_Pelicans"]
    case "NYK":
      return logos.logo_book["NY_Knicks"]
    case "New York":
      return logos.logo_book["NY_Knicks"]
    case "New York Knicks":
      return logos.logo_book["NY_Knicks"]
    case "OKC":
      return logos.logo_book["OKC_Thunder"]
    case "Oklahoma City":
      return logos.logo_book["OKC_Thunder"]
    case "Oklahoma City Thunder":
      return logos.logo_book["OKC_Thunder"]
    case "ORL":
      return logos.logo_book["ORL_Magic"]
    case "Orlando":
      return logos.logo_book["ORL_Magic"]
    case "Orlando Magic":
      return logos.logo_book["ORL_Magic"]
    case "PHI":
      return logos.logo_book["PHI_76ers"]
    case "Philadelphia":
      return logos.logo_book["PHI_76ers"]
    case "Philadelphia 76ers":
      return logos.logo_book["PHI_76ers"]
    case "PHX":
      return logos.logo_book["PHO_Suns"]
    case "PHO":
      return logos.logo_book["PHO_Suns"]
    case "Phoenix":
      return logos.logo_book["PHO_Suns"]
    case "Phoenix Suns":
      return logos.logo_book["PHO_Suns"]
    case "POR":
      return logos.logo_book["POR_Trailblazers"]
    case "Portland":
      return logos.logo_book["POR_Trailblazers"]
    case "Portland Trailblazers":
      return logos.logo_book["POR_Trailblazers"]
    case "SAC":
      return logos.logo_book["SAC_Kings"]
    case "Sacramento":
      return logos.logo_book["SAC_Kings"]
    case "Sacramento Kings":
      return logos.logo_book["SAC_Kings"]
    case "SAS":
      return logos.logo_book["SA_Spurs"]
    case "San Antonio":
      return logos.logo_book["SA_Spurs"]
    case "San Antonio Spurs":
      return logos.logo_book["SA_Spurs"]
    case "SEA":
      return logos.logo_book["SEA_Supersonics"]
    case "Seattle":
      return logos.logo_book["SEA_Supersonics"]
    case "Seattle Supersonics":
      return logos.logo_book["SEA_Supersonics"]
    case "TOR":
      return logos.logo_book["TOR_Raptors"]
    case "Toronto":
      return logos.logo_book["TOR_Raptors"]
    case "Toronto Raptors":
      return logos.logo_book["TOR_Raptors"]
    case "UTA":
      return logos.logo_book["UTA_Jazz"]
    case "Utah":
      return logos.logo_book["UTA_Jazz"]
    case "Utah Jazz":
      return logos.logo_book["UTA_Jazz"]
    case "Vancouver":
      return logos.logo_book["VAN_Sealions"]
    case "VAN":
      return logos.logo_book["VAN_Sealions"]
    case "Vancouver Sea Lions":
      return logos.logo_book["VAN_Sealions"]
    case "Washington":
      return logos.logo_book["WAS_Wizards"]
    case "WAS":
      return logos.logo_book["WAS_Wizards"]
    case "Washington Wizards":
      return logos.logo_book["WAS_Wizards"]
    case "ALBA":
      return logos.logo_book["ALBA"]
    case "ALBA Berlin":
      return logos.logo_book["ALBA"]
    case "Efes":
      return logos.logo_book["Anadolu"]
    case "Anadolu Efes":
      return logos.logo_book["Anadolu"]
    case "Barcelona":
      return logos.logo_book["Barcelona"]
    case "Bayern":
      return logos.logo_book["Bayern"]
    case "Bayern Munich":
      return logos.logo_book["Bayern"]
    case "Cazoo":
      return logos.logo_book["CazooBaskonia"]
    case "Cazoo Baskonia":
      return logos.logo_book["CazooBaskonia"]
    case "Crvena zvezda":
      return logos.logo_book["CrvenaZvezda"]
    case "Olimpia Milano":
      return logos.logo_book["Olimpia"]
    case "Fenerbahce Beko":
      return logos.logo_book["Fenerbache"]
    case "LDLC":
      return logos.logo_book["LDLC"]
    case "ASVEL":
      return logos.logo_book["LDLC"]
    case "LDLC ASVEL":
      return logos.logo_book["LDLC"]
    case "Maccabi":
      return logos.logo_book["Maccabi"]
    case "Maccabi Tel Aviv":
      return logos.logo_book["Maccabi"]
    case "Olympiacos":
      return logos.logo_book["Olympiacos"]
    case "Panathinaikos":
      return logos.logo_book["Panathinaikos"]
    case "KK Partizan":
      return logos.logo_book["KKPartizan"]
    case "Real Madrid":
      return logos.logo_book["RealMadrid"]
    case "Zalgiris":
      return logos.logo_book["Zalgiris"]
    case "London":
      return logos.logo_book["London"]
    case "London Lions":
      return logos.logo_book["London"]
    case "Caledonia":
      return logos.logo_book["Caledonia"]
    case "Caledonia Gladiators":
      return logos.logo_book["Caledonia"]
    case "Virtus Bologna":
      return logos.logo_book["Virtus"]
    case "Prometey":
      return logos.logo_book["Prometey"]
    case "VEF Riga":
      return logos.logo_book["VEF"]
    case "Beijing Ducks":
      return logos.logo_book["BeijingDucks"]
    case "Jilin Northeast Tigers":
      return logos.logo_book["Jilin"]
    case "Shandong Hi-Speed Kirin":
      return logos.logo_book["Shandong"]
    case "Guangdong Southern Tigers":
      return logos.logo_book["Guandong"]
    case "Guangzhou Loong Lions":
      return logos.logo_book["Guangzhou"]
    case "Barangay Ginebra San Miguel":
      return logos.logo_book["Barangay"]
    case "Shanghai Sharks":
      return logos.logo_book["Shanghai"]
    case "Shenzhen Leopards":
      return logos.logo_book["Shenzen"]
    case "Alvark Tokyo":
      return logos.logo_book["Alvark"]
    case "Tokyo":
      return logos.logo_book["Alvark"]
    case "Hiroshima Dragonflies":
      return logos.logo_book["Hiroshima"]
    case "Hiroshima":
      return logos.logo_book["Hiroshima"]
    case "Nagoya Diamond Dolphins":
      return logos.logo_book["Nagoya"]
    case "Nagoya":
      return logos.logo_book["Nagoya"]
    case "Taipei Fubon":
      return logos.logo_book["Taipei"]
    case "Taipei Fubon Braves":
      return logos.logo_book["Taipei"]
    case "Fubon":
      return logos.logo_book["Taipei"]
    case "Ryukyu Golden Kings":
      return logos.logo_book["Ryuku"]
    case "Seoul Samsung Thunders":
      return logos.logo_book["Seoul"]
    case "Goyang Carrot Jumpers":
      return logos.logo_book["Goyang"]
    case "Goyang":
      return logos.logo_book["Goyang"]
    case "Adelaide 36ers":
      return logos.logo_book["Adelaide"]
    case "Adelaide":
      return logos.logo_book["Adelaide"]
    case "Brisbane Bullets":
      return logos.logo_book["Brisbane"]
    case "Brisbane":
      return logos.logo_book["Brisbane"]
    case "Melbourne United":
      return logos.logo_book["Melbourne"]
    case "Melbourne":
      return logos.logo_book["Melbourne"]
    case "Perth":
      return logos.logo_book["Perth"]
    case "Perth Wildcats":
      return logos.logo_book["Perth"]
    case "New Zealand":
      return logos.logo_book["NewZealand"]
    case "New Zealand Breakers":
      return logos.logo_book["NewZealand"]
    case "Western All Stars":
      return logos.logo_book["Western"]
    case "Western Rising Stars":
        return logos.logo_book["Western"]
    case "Eastern All Stars":
      return logos.logo_book["Eastern"]
    case "Eastern Rising Stars":
        return logos.logo_book["Eastern"]
    case _:
      return ""