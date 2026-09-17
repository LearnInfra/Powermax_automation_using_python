array = "000123456789"

payload = {
    "expandStorageGroup": False,
    "num_of_vols": 5,
    "volumeIdentifier": {
        "identifier_name": "APPDB"
    },
    "volume_size": "100",
    "cap_unit": "GB"
}

url = f"{BASE_URL}/100/sloprovisioning/symmetrix/{array}/storagegroup/APP_PROD_SG/volume"

response = session.post(url, json=payload)

print(response.json())
