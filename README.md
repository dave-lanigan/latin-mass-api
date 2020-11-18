## Latin Mass API

API for information on tridentine catholic liturgies from tridentine-only societies world wide.

FSSP mass information is scraped from the [FSSP](https://www.fssp.org/en/find-us/where-are-we/) website.

SSPX mass information is scraped from the [SSPX](https://sspx.org/en) site from the various region's pages.

ICKSP mass information is

SSPV mass information is scraped from the [SSPV](https://congregationofstpiusv.com/locations/) site.

Note: SSPX and SSPV have an irregular status according to the Vatican.

***Note: Currently only fssp and sspv (usa) are available.***


### Root endpoint:


### Public Endpoints:

#### /orgs

(GET) Returns a json object with the organizations - their names in latin and english and abbreviations.

Ex. Response:

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

##### /countries/(org)

(GET) Returns a list of the countries where an organization has masses.

```
Ex: GET /countries/fssp
```

Ex. Response:

```
['Australia', 'Belgique', 'Canada', 'Colombia', 'Deutschland', 'France', 'Great Britain', 'Irlande', 'Italia', 'México', 'Nederland', 'New Zealand', 'Nigeria', 'Polska', 'Suisse', 'USA', 'Österreich', 'Česká republika']
```

##### /masses

(GET) Returns a list of json objects of masses from all different organizations and diocese. You can filter by country by passing the country in as a parameter.

Parameter | Type | Description
------|-------|-----
country | String | The country. Ex: New Zealand or new zealand.
org | String | The organization. Use the organizations abbreviation. Ex: fssp or sspv
name | String | The name of the church or building.


Ex Response:

```
[
  {
    "_id": "5fb5575d7869140237f637a9", 
    "address": "Charles O'Neill Way (off Thomas St.) - Lewisham NSW 2049 - Australia", 
    "country": "Australia", 
    "diocese": "Sydney", 
    "estDate": null, 
    "link": "http://www.maternalheart.org", 
    "name": "Maternal Heart of Mary Parish", 
    "org": "fssp", 
    "times": [
      "Sun. 8.30 and 10.30 a.m.", 
      "Mon. 7.00 a.m.", 
      "Tue. 6.00 p.m.", 
      "Wed. 7.00 a.m.", 
      "Thu. 7.00 p.m.", 
      "Fri. 6.15 p.m. (First Fri. 7.00 p.m.)", 
      "Sat. 9.00 a.m.", 
      "Public Holidays 8.00 a.m."
    ]
  }, 
  {
    "_id": "5fb5575e7869140237f637aa", 
    "address": "8-14 Austin Woodbury Place - Old Toongabbie NSW 2146 - Australia", 
    "country": "Australia", 
    "diocese": "Parramatta", 
    "estDate": null, 
    "link": null, 
    "name": "Campion College Chapel", 
    "org": "fssp", 
    "times": [
      "Fri. 12 p.m. (during term)"
    ]
  }, 
  ...

```
#####  /masses/(org)

(GET) Returns the masses specific to an organization. Use the organizations abbreviation. 


Parameter | Type | Description
------|-------|-----
country | String | The country. Ex: New Zealand or new zealand.
name | String | The name of the church or building.

```
Ex: GET /masses/fssp
```


Ex. Response

```
[
  {
    "_id": "5fb5575d7869140237f637a9", 
    "address": "Charles O'Neill Way (off Thomas St.) - Lewisham NSW 2049 - Australia", 
    "country": "Australia", 
    "diocese": "Sydney", 
    "estDate": null, 
    "link": "http://www.maternalheart.org", 
    "name": "Maternal Heart of Mary Parish", 
    "org": "fssp", 
    "times": [
      "Sun. 8.30 and 10.30 a.m.", 
      "Mon. 7.00 a.m.", 
      "Tue. 6.00 p.m.", 
      "Wed. 7.00 a.m.", 
      "Thu. 7.00 p.m.", 
      "Fri. 6.15 p.m. (First Fri. 7.00 p.m.)", 
      "Sat. 9.00 a.m.", 
      "Public Holidays 8.00 a.m."
    ]
  }, 
  {
    "_id": "5fb5575e7869140237f637aa", 
    "address": "8-14 Austin Woodbury Place - Old Toongabbie NSW 2146 - Australia", 
    "country": "Australia", 
    "diocese": "Parramatta", 
    "estDate": null, 
    "link": null, 
    "name": "Campion College Chapel", 
    "org": "fssp", 
    "times": [
      "Fri. 12 p.m. (during term)"
    ]
  }, 
  ....
```

### Private Endpoints (Must have key)

##### /(org)

(PUT) Update a Mass document for an organization.

Parameter | Type | Required |Description
------|-------|-----
id | string | Yes | The id for the mass document.
time | list | No | list of times for the mass. Ex: ["Sun. 8:00am, 10:30am","Sat. 10:00am"]
estDate | dict/obj | No | Date of establishement Should conform to ISO 8601. Ex: {"community":"1987-01-13","org":"2007-01-13","quasiParish":"2009-13-10", "parish":"2011-13-10"}


Ex. Response:
```  
{
    "_id": "5fb5575d7869140237f637a9", 
    "address": "Charles O'Neill Way (off Thomas St.) - Lewisham NSW 2049 - Australia", 
    "country": "Australia", 
    "diocese": "Sydney", 
    "estDate": null, 
    "link": "http://www.maternalheart.org", 
    "name": "Maternal Heart of Mary Parish", 
    "org": "fssp", 
    "times": [
      "Sun. 8.30 and 10.30 a.m.", 
      "Mon. 7.00 a.m.", 
      "Tue. 6.00 p.m.", 
      "Wed. 7.00 a.m.", 
      "Thu. 7.00 p.m.", 
      "Fri. 6.15 p.m. (First Fri. 7.00 p.m.)", 
      "Sat. 9.00 a.m.", 
      "Public Holidays 8.00 a.m."
    ]
  }, 

```

##### /(org)

(POST) post a mass document to the MongoDB database.

Parameter | Type | Required |Description
------|-------|-----
org | String | Yes | The organization. Use the organizations abbreviation. Ex: fssp or sspv
name | String | Yes | The name of the church or building.
country | String | Yes | The country. Ex: New Zealand.
diocese | String | No | The diocese - only required for Vatican recognized churches.
address | String | Yes | The address to the church or building. Can be null.
times | List | Yes | List of times for the mass. Ex: ["Sun. 8:00am, 10:30am","Sat. 10:00am"].
link | List | Yes | List of times for the mass. Ex: ["Sun. 8:00am, 10:30am","Sat. 10:00am"]. Can be null.
estDate | Dict/Obj | Yes | Date of establishement Should conform to ISO 8601. Ex: {"community":"1987-01-13","org":"2007-01-13","quasiParish":"2009-13-10", "parish":"2011-13-10"} 



Ex. Response:
```
  {
    "_id": "5fb5575d7869140237f637a9", 
    "address": "Charles O'Neill Way (off Thomas St.) - Lewisham NSW 2049 - Australia", 
    "country": "Australia", 
    "diocese": "Sydney", 
    "estDate": null, 
    "link": "http://www.maternalheart.org", 
    "name": "Maternal Heart of Mary Parish", 
    "org": "fssp", 
    "times": [
      "Sun. 8.30 and 10.30 a.m.", 
      "Mon. 7.00 a.m.", 
      "Tue. 6.00 p.m.", 
      "Wed. 7.00 a.m.", 
      "Thu. 7.00 p.m.", 
      "Fri. 6.15 p.m. (First Fri. 7.00 p.m.)", 
      "Sat. 9.00 a.m.", 
      "Public Holidays 8.00 a.m."
    ]
  }, 

```

##### /(org)

(DELETE) Delete a mass document from the MongoDB database.

Parameter | Type | Description
------|-------|-----
id | string | The id for the mass document.


Ex. Response:
```
{"status":"success"}

```
