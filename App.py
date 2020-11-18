from flask import Flask, jsonify, request
import os
import pymongo
import json


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


def find_all(curser):
    out = list(curser)
    l = []
    for i, mass in enumerate(out):
        del mass["_id"]
        l.append(mass)
    return l


@app.route(os.path.join(conf["root"], 'orgs'), methods=['GET'])
def get_orgs():
    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]
    org_key = db["org_key"].find_one()
    del org_key['_id']
    return jsonify(org_key)


@app.route(os.path.join(conf["root"], 'countries/<org>'), methods=['GET'])
def get_orgs_countries(org):
    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]
    coll = db[org]
    return jsonify(coll.find().distinct("country"))

# what is this? use a decorator to route


@app.route(os.path.join(conf["root"], 'masses'), methods=['GET'])
def get_all_masses():
    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]

    coll1 = client["masses"]["fssp"]
    coll2 = client["masses"]["sspv"]

    if len(request.args) != 0:
        if "country" in list(request.args.keys()):
            country = request.args["country"].title()
            if country in ["United States", "United States of America"]:
                country = "USA"
            request.args["country"] = country

        out = find_all(coll1.find(request.args)) + \
            find_all(coll2.find(request.args))

        return jsonify(out)

    if len(request.args) == 0:
        out = find_all(coll1.find()) + find_all(coll2.find())

        return jsonify(out)


@app.route(os.path.join(conf["root"], 'masses/<org>'), methods=['GET'])
def get_org_masses(org):

    client = pymongo.MongoClient(conf["mongo"])
    db = client["masses"]

    if org == "fssp":
        coll = client["masses"]["fssp"]
        return jsonify(find_all(coll))

    elif org == "sspv":
        coll = client["masses"]["sspv"]
        return jsonify(find_all(coll))

    elif org == "sspx":
        coll = client["masses"]["sspv"]
        return jsonify(find_all(coll))

    elif org == "icksp":
        coll = client["masses"]["sspv"]
        return jsonify(find_all(coll))


@app.route('/masses/<organization>/<id>', methods=['POST'])
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


@app.route(os.path.join(conf["root"], 'test'), methods=['GET', 'POST'])
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
