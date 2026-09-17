import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json

urllib3.disable_warnings()

# Unisphere Details
UNISPHERE = "https://unisphere.company.com:8443"
USERNAME = "admin"
PASSWORD = "password"

# Arrays
SOURCE_SID = "000123456789"
TARGET_SID = "000987654321"

# SRDF Configuration
RDF_GROUP = "10"
SOURCE_SG = "APP_PROD_SG"
TARGET_SG = "APP_DR_SG"

BASE_URL = f"{UNISPHERE}/univmax/restapi"
API_VERSION = "100"

session = requests.Session()
session.auth = HTTPBasicAuth(USERNAME, PASSWORD)
session.verify = False
session.headers.update({
    "Content-Type": "application/json",
    "Accept": "application/json"
})

payload = {
    "executionOption": "SYNCHRONOUS",
    "rdfgNumber": RDF_GROUP,
    "remoteSymmID": TARGET_SID,
    "remoteStorageGroupName": TARGET_SG,
    "createRdfPair": True
}

url = (
    f"{BASE_URL}/{API_VERSION}/replication/"
    f"symmetrix/{SOURCE_SID}/storagegroup/{SOURCE_SG}/rdf_group"
)

response = session.post(url, json=payload)

print("Status Code:", response.status_code)
print(json.dumps(response.json(), indent=4))
