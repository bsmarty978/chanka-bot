import pymongo
import pandas as pd
client = pymongo.MongoClient("mongodb+srv://nameless_gambit:smtG886611@cluster0.zjdqc.mongodb.net/R6SDB?retryWrites=true&w=majority")
db = client.dbr6s
players = db.Players
res = players.find({ '$text' : {'$search' : '^.*pengu.*$'}})
print(res.count())
result = res[0]
# print(result)
print(result['ign'])
print(result['name'])
print(result['photo'])
print(result['country'])
statsdf = pd.DataFrame(res[0]['allstats'])
statsdf.set_index('match_id',inplace=True)
avgs =  statsdf.max()
print(avgs)