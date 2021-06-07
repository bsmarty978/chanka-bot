import json
from bson import json_util
import time
import dateparser as dp
from datetime import datetime as dt
import pymongo
import pandas as pd

start = time.time()
# with open("result2jun.json","r") as f:
#     d = f.read()

data = json.load(open("r2-jun-21.json",encoding="utf-8"))


#Methods

#Sorts matches according to datetime.
def matchesDatetime(dataobject):
    for d in data:
        d['time_obj'] = dp.parse(d['time'])
        d['match_id'] = int(d['match_id'])
        if d['result_a']!='-':
            d['result_a'] = float(d['result_a'])
        else:
            d['result_a'] = 0.0
        if d['result_b']!='-':
            d['result_b'] = float(d['result_b'])
        else:
            d['result_b'] = 0.0

        if d['stats']!=[]:
            for s in d['stats']:
                s['rating'] = float(s['rating'])
                s['kpr'] = float(s['kpr'])
                s['1vx'] = int(s['1vx'])
                s['plant'] = int(s['plant'])

                s['hs'] = int(s['hs'].split('%')[0])
                s['kost'] = int(s['kost'].split('%')[0])
                s['srv'] = int(s['srv'].split('%')[0])
                
                #new attributes 
                s['kill'] = int(s['kd'].split('(')[0].split('-')[0])
                s['death'] = int(s['kd'].split('(')[0].split('-')[1])

                s['entry_kill'] = int(s['entry'].split('(')[0].split('-')[0])
                s['entry_death'] = int(s['entry'].split('(')[0].split('-')[1])


    data.sort(key=lambda r:r["time_obj"])
    return data

#Return all the players in given dataobject with every match stats of each plaeyer.
def allplayers(dataobject):
    players_dict={}
    players_list = []
    for items in dataobject:
        match_id = items["match_id"]
        team_a = items["team_a"]["name"]
        team_b = items["team_b"]["name"]
        roster_a = items["roster"]['team_a']
        roster_b = items["roster"]['team_b']
        time = items["time_obj"]
        for playerdetail in items["player_details"]:
            ign = playerdetail['ign']
            name = playerdetail['name']
            country = playerdetail['country']
            photo = playerdetail['photo']

            if ign in roster_a:
                player_team = team_a
            elif ign in roster_b:
                player_team = team_b
            else:
                player_team = "WildEntry"

            if ign in list(players_dict.keys()):
                if players_dict[ign]['name'] == "":
                    players_dict[ign]['name'] = name
                if players_dict[ign]['country'] == "":
                    players_dict[ign]['country'] = country
                if players_dict[ign]['photo'] == "":
                    players_dict[ign]['photo'] = photo
                if player_team not in list(players_dict[ign]['teams'].keys()):
                    players_dict[ign]['teams'][player_team] = time
            else:
                players_dict[ign] = {}
                players_dict[ign]['ign'] = ign
                players_dict[ign]['name'] = name
                players_dict[ign]['photo'] = photo
                players_dict[ign]['country'] = country
                players_dict[ign]['teams'] = {}
                players_dict[ign]['teams'][player_team] = time
                players_dict[ign]['allstats'] = []

        stats_p = []
        for p in items["stats"]:
            stats_p.append(p['name'])

        # player Rating and Player List
        for player in items["stats"]:
            ign = player["name"]
            player_stat = player
            player_stat['match_id'] = match_id
            del player_stat['name']
            if ign in roster_a:
                player_team = team_a
            elif ign in roster_b:
                player_team = team_b
            else:
                awild = not(all(p in stats_p for p in roster_a))
                bwild = not(all(p in stats_p for p in roster_b))
                if awild and bwild:
                    player_team = "WildEntry"
                elif awild:
                    player_team = team_a
                else:
                    player_team = team_b
            try:
                players_dict[ign]['allstats'].append(player_stat)
            except KeyError:
                players_dict[ign] = {}
                players_dict[ign]['ign'] = ign
                players_dict[ign]['name'] = ""
                players_dict[ign]['photo'] = ""
                players_dict[ign]['country'] = ""
                players_dict[ign]['teams'] = {}
                players_dict[ign]['teams'][player_team] = time
                players_dict[ign]['allstats'] = []
                players_dict[ign]['allstats'].append(player_stat)



    for id,player in enumerate(players_dict):
        ply = players_dict[player]
        ign = ply['ign']
        name = ply['name']
        photo = ply['photo']
        country = ply['country']
        allstats = ply['allstats']
        timeline = []
        for team in ply['teams']:
            timeline.append({
                'teamname' : team,
                'jointime' : ply['teams'][team]
            })

        players_list.append({
            'playerid':id+1,
            'ign' : ign,
            'name':name,
            'photo' : photo,
            'country': country,
            'aliases': [ign.lower(),ign.upper()],
            'total matches':len(allstats),
            'timeline' : timeline,
            'allstats': allstats
            })

    return players_list

#To save data into local Json File.
def localJSONsave(objectlist,filename):
    with open(f"{filename}.json","w", encoding='utf-8') as fd:
        # fd.write(json.dumps(objectlist))
        fd.write(json.dumps(objectlist, default=json_util.default))

#To add Images of player into their player object.
def PlayerImgUrl(objectlist,players):
    photo_dict={}
    for items in objectlist:
        for item in items["photos"]:
            if items["photos"][item] != None:
                photo_dict[item] = items["photos"][item]
            else:
                photo_dict[item] = "https://siege.gg/img/player-silhouette-darker.svg"

    for player in players:
        try:
            player["photo"] = photo_dict[player["name"]]
        except KeyError:
            player["photo"] = "https://siege.gg/img/player-silhouette-darker.svg"
        
    return players


sorted_data = matchesDatetime(data)
print("sorted")
players = allplayers(sorted_data)


#NOTE: To insetr data to MONGODB ATLAS
# client = pymongo.MongoClient("mongodb+srv://nameless_gambit:smtG886611@cluster0.zjdqc.mongodb.net/R6SDB?retryWrites=true&w=majority")
# db = client.dbr6s

# ply_col = db.Players

# ply_col.insert_many(players)

print(len(players))
end = time.time()
print(end - start)