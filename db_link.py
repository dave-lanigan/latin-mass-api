import pymongo
from bson.json_util import dumps as bdumps
import json


with open("config.json", "r") as f:
    conf = json.load(f)

client = pymongo.MongoClient(conf["mongo"])
db = client["masses"]

coll1 = db["fssp"]
coll2 = db["sspv"]

#coll = coll1+coll2

out = list(coll1.find(
    {"country": "USA", "name": "St. Joseph the Worker Parish"}))

out1 = list(coll1.find({}))
out2 = list(coll1.find())

print(len(out1), len(out2))

print(list(out))
