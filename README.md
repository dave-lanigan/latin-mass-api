# Latin Mass API

API for information on tridentine catholic liturgies world wide.

FSSP mass information is scraped from the [FSSP](https://www.fssp.org/en/find-us/where-are-we/) website.

SSPX mass information is scraped from the [SSPX](https://sspx.org/en) site from the various region's pages.

SSPV mass information is scraped from the [SSPV](https://congregationofstpiusv.com/locations/) site.

Note: SSPX and SSPV have an irregular status according to the Vatican.

***Note: Currently only fssp and sspv (usa) are available.***


### Root endpoint:


### Endpoints:

Request:

```
GET /organizations
```

Response:

```
{
  "fssp": {
    "english": "Priestly Fraternity of Saint Peter",
    "latin": "Fraternitas Sacerdotalis Sancti Petri"
  },
  "sspv": {
    "english": "Society of Saint Pius V",
    "latin": "Societas Sacerdotalis Sancti Pii Quinti"
  },
  "sspx": {
    "english": "Society of Saint Pius X",
    "latin": "Fraternitas Sacerdotalis Sancti Pii X"
  }
}

```
Request:

```
GET /masses
```

Response:
- Returns a list of json objects of masses from all different organizations and diocese

```
[
  {
    "address": "Charles O'Neill Way (off Thomas St.) - Lewisham NSW 2049 - Australia", 
    "country": "Australia", 
    "diocese": "Sydney", 
    "estDate0": null, 
    "link": "http://www.maternalheart.org", 
    "times": [
      "Sun. 8.30 and 10.30 a.m.", 
      "Mon. 7.00 a.m.", 
      "Tue. 6.00 p.m.", 
      "Wed. 7.00 a.m.", 
      "Thu. 7.00 p.m.", 
      "Fri. 6.15 p.m. (First Fri. 7.00 p.m.)", 
      "Sat. 9.00 a.m.", 
      "Public Holidays 8.00 a.m."
    ], 
    "name": "Maternal Heart of Mary Parish", 
    "org": "fssp"
  }, 
  {
    "address": "8-14 Austin Woodbury Place - Old Toongabbie NSW 2146 - Australia", 
    "country": "Australia", 
    "diocese": "Parramatta", 
    "estDate0": null, 
    "link": null, 
    "times": [
      "Fri. 12 p.m. (during term)"
    ], 
    "name": "Campion College Chapel", 
    "org": "fssp"
  }, 
  {
    "address": "70 Douglas Rd - Blacktown NSW 2148 - Australia", 
    "country": "Australia", 
    "diocese": "Parramatta", 
    "estDate0": null, 
    "link": null, 
    "times": [
      "Sun. 8am, 10am (Sung)"
    ], 
    "name": "Croatian Catholic Parish Hall", 
    "org": "fssp"
  },

```
Request:

```
GET /masses/fssp
```

Response:
- Returns a list of json objects of masses from fssp

```
[
  {
    "address": "Charles O'Neill Way (off Thomas St.) - Lewisham NSW 2049 - Australia", 
    "country": "Australia", 
    "diocese": "Sydney", 
    "estDate0": null, 
    "link": "http://www.maternalheart.org", 
    "times": [
      "Sun. 8.30 and 10.30 a.m.", 
      "Mon. 7.00 a.m.", 
      "Tue. 6.00 p.m.", 
      "Wed. 7.00 a.m.", 
      "Thu. 7.00 p.m.", 
      "Fri. 6.15 p.m. (First Fri. 7.00 p.m.)", 
      "Sat. 9.00 a.m.", 
      "Public Holidays 8.00 a.m."
    ], 
    "name": "Maternal Heart of Mary Parish", 
    "org": "fssp"
  }, 
  {
    "address": "8-14 Austin Woodbury Place - Old Toongabbie NSW 2146 - Australia", 
    "country": "Australia", 
    "diocese": "Parramatta", 
    "estDate0": null, 
    "link": null, 
    "times": [
      "Fri. 12 p.m. (during term)"
    ], 
    "name": "Campion College Chapel", 
    "org": "fssp"
  }, 
  {
    "address": "70 Douglas Rd - Blacktown NSW 2148 - Australia", 
    "country": "Australia", 
    "diocese": "Parramatta", 
    "estDate0": null, 
    "link": null, 
    "times": [
      "Sun. 8am, 10am (Sung)"
    ], 
    "name": "Croatian Catholic Parish Hall", 
    "org": "fssp"
  },
  ....
```
