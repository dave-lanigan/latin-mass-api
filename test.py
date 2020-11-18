import requests
import pymongo
import json


class Test:
    def __init__(self, root):
        self.root = root

    def test_orgs_countries(self, org):
        passed = False
        path = self.root+"countries/{}".format(org)
        resp = requests.get(path).json()

        if type(resp) == list:
            passed = True

        print("Enpoint: {} Passed: {}".format(path, passed))
        return resp, passed

    def test_orgs_countries(self, org):
        passed = False
        path = self.root+"countries/{}".format(org)
        resp = requests.get(path).json()

        if type(resp) == list:
            passed = True

        print("Enpoint: {} Passed: {}".format(path, passed))
        return resp, passed


# query parameters
#payload = {"country": "usa"}
# out = requests.get(root+url, params=payload)

# print(help(out))

# out = requests.get(
#     root+url, params=payload)
# print(out.content)

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

if __name__ == "__main__":

    with open("config.json", "r") as f:
        conf = json.load(f)

    ROOT = "http://127.0.0.1:5000/"+conf["root"]
    SECRET_KEY = conf["secret-key"]

    testing = Test(ROOT)

    t1, _ = testing.test_orgs_countries("fssp")
