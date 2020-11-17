# latin-mass-API

API for information on wordwide.
Currently only fssp and sspv (usa) are available.

#### Endpoints

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
