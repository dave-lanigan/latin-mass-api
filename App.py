from flask import Flask, jsonify
import requests
import os
import pymongo
import json

# init app

app = Flask(__name__)


# what is this? use a decorator to route
@app.route('/organizations', methods=['GET'])
def get_orgs():
    client = pymongo.MongoClient(
        "mongodb+srv://david:Davlan240!@cluster0.4kpiq.mongodb.net/masses?retryWrites=true&w=majority")
    db = client["masses"]
    org_key = db["org_key"].find_one()
    del org_key['_id']
    return jsonify(org_key)


@app.route('/masses', methods=['GET'])
def get_all_masses():
    client = pymongo.MongoClient(
        "mongodb+srv://david:Davlan240!@cluster0.4kpiq.mongodb.net/masses?retryWrites=true&w=majority")
    db = client["masses"]
    fssp = db["fssp"].find_one()
    sspv = db["sspv"].find_one()
    del fssp['_id']
    del sspv['_id']

    return jsonify(fssp.update(sspv))


@app.route('/masses/fssp', methods=['GET'])
def get_fssp_masses():
    client = pymongo.MongoClient(
        "mongodb+srv://david:Davlan240!@cluster0.4kpiq.mongodb.net/masses?retryWrites=true&w=majority")
    coll = client["masses"]["fssp"]
    fssp = list(coll.find())
    d = []
    for i, mass in enumerate(fssp):
        del mass["_id"]
        d.append(mass)
    return jsonify(fssp)


if __name__ == "__main__":
    app.run(debug=True)
