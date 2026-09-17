payload = {
    "action": "Failover"
}

response = session.post(
    f"{BASE_URL}/{API_VERSION}/replication/symmetrix/"
    f"{SOURCE_SID}/storagegroup/{SOURCE_SG}/rdf_group/{RDF_GROUP}",
    json=payload
)

print(response.json())
