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

        if type(resp[0]) == dict:
            passed = True

        print("Endpoint: {} Passed: {}".format(path, passed))
        return resp, passed

    def test_orgs_countries(self, org):
        passed = False
        path = self.root+"countries/{}".format(org)
        resp = requests.get(path).json()

        if type(resp) == list:
            passed = True

        print("Endpoint: {} Passed: {}".format(path, passed))
        return resp, passed

    def test_orgs_masses(self, org, name="St. Joseph the Worker Parish", country="United States"):
        passed = True
        path = self.root+"masses/{}".format(org)
        resp1 = requests.get(path).json()
        resp2 = requests.get(path).json()

        if type(resp1) != list:
            passed = False

        if type(resp1[0]) != dict:
            passed = False

        if org == "fssp":
            if type(resp2[0]) != dict:
                passed = False

        print("Endpoint: {} Passed: {}".format(path, passed))
        return resp1, resp1[0], resp2[0], passed


if __name__ == "__main__":

    with open("config.json", "r") as f:
        conf = json.load(f)

    ROOT = "http://127.0.0.1:5000/"+conf["root"]
    SECRET_KEY = conf["secret-key"]

    testing = Test(ROOT)

    t0, _ = testing.test_orgs()
    t1, _ = testing.test_orgs_countries("fssp")
    t3, r3, r2, r1 = testing.test_orgs_masses(
        "fssp", name="St. Joseph the Worker Parish", country="United States")
