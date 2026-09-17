url = (
    f"{BASE_URL}/{API_VERSION}/replication/"
    f"symmetrix/{SOURCE_SID}/storagegroup/{SOURCE_SG}"
)

response = session.get(url)

data = response.json()

print(json.dumps(data, indent=4))
`
