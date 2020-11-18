import requests
import pymongo
import json


class Test:
    def __init__(self, root):
        self.root = root

    def test_orgs(self):
        passed = False
        path = self.root+"orgs"
        resp = requests.get(path).json()

        if type(resp) == dict:
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


if __name__ == "__main__":

    with open("config.json", "r") as f:
        conf = json.load(f)

    ROOT = "http://127.0.0.1:5000/"+conf["root"]
    SECRET_KEY = conf["secret-key"]

    testing = Test(ROOT)

    t0, _ = testing.test_orgs()
    t1, _ = testing.test_orgs_countries("fssp")
