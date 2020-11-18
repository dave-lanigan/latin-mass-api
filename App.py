from flask import Flask, jsonify, request, Response
import os
import pymongo
import json
from bson.json_util import dumps as bdumps


# https://linoxide.com/tools/how-to-use-curl-command/
# curl -X POST -H "Content-Type: application/json" -d '{"hell":"no"}' http://127.0.0.1:5000/test

"""
update mass times*** (hidden)
update estDate0 (hidden)
add estDate0 (hidden)

http:
body,header params, query options

"""

with open("config.json", "r") as f:
    conf = json.load(f)


# init app

app = Flask(__name__)


def parse_bson(curser):
    out = list(curser)
    l = []
    for i, mass in enumerate(out):
        mass["_id"] = str(mass["_id"])
        l.append(mass)
    return l


@app.route(os.path.join(conf["root"], 'orgs'), methods=['GET'])
def get_orgs():
    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]
    coll = db["org_key"]

    return jsonify(parse_bson(coll.find()))


@ app.route(os.path.join(conf["root"], 'countries/<org>'), methods=['GET'])
def get_orgs_countries(org):
    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]
    coll = db[org]
    return jsonify(coll.find().distinct("country"))

# what is this? use a decorator to route


@ app.route(os.path.join(conf["root"], 'masses'), methods=['GET'])
def get_all_masses():
    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]

    coll1 = client["masses"]["fssp"]
    coll2 = client["masses"]["sspv"]

    out = parse_bson(coll1.find(request.args)) + \
        parse_bson(coll2.find(request.args))

    return jsonify(out)


@ app.route(os.path.join(conf["root"], 'masses/<org>'), methods=['GET'])
def get_org_masses(org):

    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]

    coll = client["masses"][org]

    out = parse_bson(coll.find(request.args))

    return jsonify(out)


@ app.route('/masses/<organization>/<id>', methods=['POST'])
def update_masses():
    """Return all masses usa.

    Options: filter by state
    """
    # add options
    location = request.args.get('location')

    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]
    fssp = db["fssp"].find_one()
    sspv = db["sspv"].find_one()
    del fssp['_id']
    del sspv['_id']

    return jsonify(fssp.update(sspv))


@ app.route(os.path.join(conf["root"], 'test'), methods=['GET', 'POST'])
def get_test():

    # msg = request.args.get()
    request.get_data()
    msg = request.data

    # get header info
    msg = dict(request.headers)

    # get query parameters:
    args = request.args

    u = request.url
    # request.json
    f = request.form
    # msg = request.get_json()
    # return jsonify(msg)
    return jsonify({"headers": msg, "args": args, "form": f, "url": u})


if __name__ == "__main__":
    app.run(debug=True)
