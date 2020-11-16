"""
Script scraps site with selenium

"""


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
import os
import time
import json
import regex
import pymongo

os.environ['MOZ_HEADLESS'] = '1'


def create_new_filename(path="", filename=""):

    fs = os.listdir(path)
    count = 0
    for f in fs:
        if filename in f:
            count += 1
    return "{}-{}.json".format(filename, count)


def get_fssp(path="{}/data".format(os.getcwd()), collection=None):
    """Returns only masses.
    """

    def get_church_info(raw_text):
        """Only get churches places with masses.

        """
        text = raw_text
        masses = ["Masses", "Messes", "Hl. Messen"]
        dioceses = ["Diocese", "Diocèse", "Diözese"]

        for i, m in enumerate(masses):
            if len(regex.findall(m, text)) != 0:
                get_d = regex.search(dioceses[i], text)
                get_m = regex.search(m, text)

                cs = regex.search(":", text)

                dio = text[cs.span()[1]: get_m.span()[0]]
                dio = dio.strip()

                text = text[get_m.span()[0]:]

                cs = regex.search(":", text)
                masst = text[cs.span()[1]:]
                masst = masst.strip()
                masst = masst.split("/")
                for i, m in enumerate(masst):
                    masst[i] = m.strip()

                return (dio, masst)

    def get_link(td):
        link_array = td.find_all("a")
        if len(link_array) != 0:
            return str(td.find_all("a")[0]).split('"')[1]
        elif len(link_array) == 0:
            return None

    def get_country(raw_text):
        text = raw_text.strip()
        return text.split("-")[-1].strip()

    driver = webdriver.Firefox()
    driver.get('https://www.fssp.org/en/find-us/where-are-we/')
    time.sleep(5)
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'lxml')

    out = soup.find_all("tbody")[0].find_all("tr")

    driver.quit()

    d = {}
    idx = 0
    for i, el in enumerate(out):

        tds = el.find_all("td")
        info = get_church_info(tds[3].text)

        if info is None:
            pass

        else:

            doc = {
                "org": "fssp",
                "name": tds[1].text.strip(),
                "country": get_country(tds[2].text),
                "diocese": info[0],
                "address": tds[2].text.strip(),
                "masses": info[1],
                "link": get_link(tds[4]),
                "estDate0": None,
            }

            label = "mass-{}".format(idx)
            d[label] = doc
            idx += 1
            if collection:
                collection.insert(doc)

    print("fssp mongodb collection updated.")

    newf = create_new_filename(path=path, filename="fssp")

    with open("{}/{}".format(path, newf), "w") as outfile:
        json.dump(d, outfile)

    print("json backup added.")
    return d


def get_sspv():

    d = {
        "mass-0": {
            "name": "Our Lady of Sorrows Chapel",
                    "country": "United States",
                    "state": "Florida",
                    "address": "1610 North Temple Avenue (U.S. 301) Starke, FL 32091",
                    "masses": "Mass offered by the priests of the Congregation of St. Pius V on the 2nd, 3rd, 4th, and 5th Sundays of the month at 9:00 a.m.",
                    "phone": "352.226.6337",
                    "note": "Please call to verify times.",
                    "estDate0": None,
        },
        "mass-1": {
            "name": "Our Lady of Peace Chapel",
                    "country": "United States",
                    "state": "Florida",
                    "address": "2121 South Seacrest Blvd. Boynton, FL 33435",
                    "masses": "Mass every Sunday at 5:00 p.m.",
                    "phone": "954.214.5019",
                    "note": "Please call to verify times.",
                    "estDate0": None,
        },
        "mass-2": {
            "name": "Our Lady of Guadalupe Mission",
                    "country": "United States",
                    "state": "Idaho",
                    "address": "Idaho Falls Skyline Center 1575 N. Skyline Drive Idaho Falls, ID 83402",
                    "masses": "Mass every Sunday at 5:00 p.m.",
                    "phone": "208.684.4598",
                    "note": "Mass offered on the 4th Sunday of every month at 8:30 a.m.",
                    "estDate0": None,
        },
        "mass-3": {
            "name": "Sacred Heart Mission",
                    "country": "United States",
                    "state": "Illinois",
                    "address": "Idaho Falls Skyline Center 1575 N. Skyline Drive Idaho Falls, ID 83402",
                    "masses": "Mass offered on the 1st, 2nd, 3rd, and 5th Sunday",
                    "phone": "708.928.1705",
                    "note": "Please call to verify times.",
                    "estDate0": None,
        },
        "mass-4": {
            "name": "Our Lady of Grace Mission",
                    "country": "United States",
                    "state": "Kentucky",
                    "address": "Comfort Suites Airport 6535 Paramount Park Dr. Louisville, Kentucky",
                    "masses": "Mass offered on the 3rd and 5th Sundays at 8:30 a.m.",
                    "phone": "502.964.0740",
                    "note": "Please call to verify times.",
                    "estDate0": None,
        },
        "mass-5": {
            "name": "St. Hilary's Church",
                    "country": "United States",
                    "state": "Maryland",
                    "address": "3823 Second Street Brooklyn, MD 21225",
                    "masses": "Mass offered every Sunday 1st, 2nd, and 3rd Sundays – Mass is at 9 a.m.",
                    "phone": "410.355.3345",
                    "note": "Please call to verify times.",
                    "estDate0": None,
        },
        "mass-6": {
            "name": "Our Lady of Fatima Chapel",
                    "country": "United States",
                    "state": "Michigan",
                    "address": "5037 Co. Hwy. 633 Traverse City, MI 49637",
                    "masses": "Mass offered on the 1st, 2nd and 5th Sundays of the month at 9:00 a.m.",
                    "phone": "231.947.4568",
                    "note": "Please call to verify times.",
                    "estDate0": None,
        },
        "mass-7": {
            "name": "Our Lady of the Rosary Chapel",
                    "country": "United States",
                    "state": "Minnesota",
                    "address": "5820 Viola Road, N.E. Rochester, MN 55902",
                    "masses": "Mass offered on the 3rd and 5th Sundays of the month.",
                    "phone": "507.534.3682",
                    "note": "Please call to verify times.",
                    "estDate0": None,
        },
        "mass-8": {
            "name": "St. Peter’s Chains Mission",
                    "country": "United States",
                    "state": "Missouri",
                    "address": "Located in the St. Louis, MO Please call for directions.",
                    "masses": "Mass offered on the 1st, 3rd, and 5th Sundays of the month at 8:30 a.m.",
                    "phone": "314.428.9086",
                    "note": "Please call to verify times.",
                    "estDate0": None,
        },
        "mass-9": {
            "name": "St. Pius V Chapel",
                    "country": "United States",
                    "state": "New York",
                    "address": "Eight Pond Place Oyster Bay Cove, NY 11771",
                    "masses": "Mass offered every Sunday 7:00 a.m. and 8:30 a.m.",
                    "phone": "516.922.5430",
                    "note": "Holy Days of Obligation please check church bulletin.",
                    "estDate0": None,
        },
        "mass-10": {
            "name": "St. Pius V School",
                    "country": "United States",
                    "state": "New York",
                    "address": "18 Old East Neck Road Melville, NY 11747",
                    "masses": "Mass offered every Sunday 8:00 a.m. and 10:30 a.m.",
                    "phone": "631.351.0116",
                    "note": "Holy Days of Obligation and Daily Mass times please check church bulletin.",
                    "estDate0": None,
        },
        "mass-11": {
            "name": "Holy Name of Mary Church",
                    "country": "United States",
                    "state": "New York",
                    "address": "588 Winton Road North Rochester, NY 14610",
                    "masses": "Mass offered every Sunday at 8:30 a.m. Holy Days at 8:00 a.m.",
                    "phone": "516.922.5430",
                    "note": "Holy Days of Obligation and Daily Mass times please check church bulletin.",
                    "estDate0": None,
        },
        "mass-12": {
            "name": "St. Joseph’s Novitiate",
                    "country": "United States",
                    "state": "New York",
                    "address": "1275 Heart’s Content Road Round Top, NY 12473",
                    "masses": "Mass offered every Sunday 8:00 a.m. and 10:30 a.m.",
                    "phone": "518.622.9833",
                    "note": "Please call for times of Holy Day and daily Masses.",
                    "estDate0": None,
        },
        "mass-13": {
            "name": "St. Thomas More Church",
                    "country": "United States",
                    "state": "New York",
                    "address": "738 Roberts Street Utica, NY 13502",
                    "masses": "Mass offered every Sunday at 12:30 p.m. Holy Days at 12:00 p.m.",
                    "phone": "315.733.9449",
                    "note": "",
                    "estDate0": None,
        },
        "mass-14": {
            "name": "Holy Nativity Chapel",
                    "country": "United States",
                    "state": "Pennsylvania",
                    "address": "Rt. 512 Nazareth, PA 18064",
                    "masses": "Mass offered every Sunday at 12:30  p.m.",
                    "phone": "610.863.6049",
                    "note": "",
                    "estDate0": None,
        },
        "mass-15": {
            "name": "Visitation Chapel",
                    "country": "United States",
                    "state": "Pennsylvania",
                    "address": "1614 West Southern Avenue South Williamsport, PA 17702",
                    "masses": "Mass offered every Sunday at 8:15 a.m.",
                    "phone": "570.323.5124",
                    "note": "",
                    "estDate0": None,
        },
    }

    def search_names(tag_list):
        out = []
        for i, tag in enumerate(tag_list):
            if tag.text != "":
                out.append((i, tag.text.strip()))
        return out

    def insert_info(label, name, state, address, masses):

        d[label] = {
            "name": name,
            "country": "United States",
            "state": state,
            "address": address,
            "masses": masses,
            "estDate0": None,
        }

    def get_info_spans1(spans_list):
        l = []
        for span in spans_list:
            l.append(span.text)

        g = " ".join(l)
        s = g.split("……")

        splits = []
        for el in s:
            print("here")
            print(el)
            m = el.split("  ")
            print(m)
            for j, jk in enumerate(m):
                m[j] = jk.strip()

            splits.append(el.split("  "))

        return splits

    keys = list(d.keys())

    # def get_info_spans2(spans_list):
    #         l = []
    #     for span in spans_list:
    #         l.append(span.text)

    #     g = " ".join(l)
    #     s = g.split("……")

    #     splits = []
    #     for el in s:
    #         print("here")
    #         print(el)
    #         m = el.split("  ")
    #         print(m)
    #         for j, jk in enumerate(m):
    #             m[j] = jk.strip()

    #         splits.append(el.split("  "))

    #     return splits

    # url = "https://congregationofstpiusv.com/locations/"

    # user_agent = {'User-agent': 'Mozilla/5.0'}
    # page = requests.get(url2, headers=user_agent).content
    # soup = BeautifulSoup(page, "lxml")

    # driver = webdriver.Firefox()
    # driver.get(url)
    # time.sleep(3)
    # page_source = driver.page_source

    # soup = BeautifulSoup(page_source, 'lxml')

    # # print(soup.prettify())
    # out = soup.find_all(class_="et_pb_toggle_content clearfix")
    # states = soup.find_all(class_="et_pb_toggle_title")

    # print(get_info_spans(out[1].find_all("span")))
    # print(search_names(out[0].find_all("strong")))
    # print(search_names(out[0].find_all("strong")))

    # d = {}
    # for i, el in enumerate(out):
    #     state = states[i].text.strip()
    #     if state not in ["Idaho", "Illinois", "Kentucky", "Maryland"]:
    #         nl = search_names(el.find_all("strong"))
    #         splits = get_info_spans(el.find_all("span"))
    #         for j, el2 in enumerate(nl):

    #             print(len(splits[j]))
    #             print(splits[j])

    #             label = "mass-{}".format(i+j)
    #             address = splits[j][0] + " " + splits[j][1]
    #             masses = splits[j][3]
    #             name = el2[1]

    #             print(label, name, address)
    #             insert_info(label, name, state, address, masses)

    #         print(d)

    # if len(nl) == 1:
    #     label = "mass-{}".format(i+j)

    #     insert_info(label, name, states[i], address, masses)`

    return d


def get_sspx():
    url = "https://sspx.org/en/community/priories"
    urls = [""]

    page = requests.get(url).content
    soup = BeautifulSoup(page, "lxml")

    sections = soup.find_all("section")

    print(sections[2])

    print(sections[2].find_all("h2")[0].text)

    d = {}
    for i, section in enumerate(sections):

        label = "mass-{}".format(i)

        d[label] = {
            "name": section.find_all("h2")[0].text.strip(),
            "country": "United States",
            "address": tds[2].text.strip(),
            "link": get_link(tds[4]),
            "estDate0": None,
            "phone": None}


if __name__ == "__main__":

    client = pymongo.MongoClient(
        "mongodb+srv://david:Davlan240!@cluster0.4kpiq.mongodb.net/masses?retryWrites=true&w=majority")
    db = client["masses"]

    get_fssp(collection=db["fssp"])
    # get_fssp(collection=None)
