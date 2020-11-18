import requests
import pymongo
import json


root = "http://127.0.0.1:5000/api/v0/"
url = "masses"


# query parameters
payload = {"country": "usa"}
# out = requests.get(root+url, params=payload)

# print(help(out))

out = requests.get(
    root+url, params=payload)
print(out.content)

# with open("config.json", "r") as f:
#     conf = json.load(f)

# client = pymongo.MongoClient(conf["mongo"])
# db = client["masses"]

# coll1 = db["fssp"]
# coll2 = db["sspv"]

# #coll = coll1+coll2

# print(coll1.find().distinct("country"))
# print(out.next())
# .where()

#what is map/reduce


# for el in list(out):
#     print(el)
#     print(" ")
