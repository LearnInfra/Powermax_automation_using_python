import requests
import pandas as pd

array_id = "000123456789"

url = f"{BASE_URL}/100/sloprovisioning/symmetrix/{array_id}/srp"

resp = session.get(url)
resp.raise_for_status()

records = []

for srp in resp.json()["srpId"]:
    details = session.get(
        f"{url}/{srp}"
    ).json()

    records.append({
        "SRP": srp,
        "Used_TB": details["total_used_cap_gb"] / 1024,
        "Allocated_TB": details["total_allocated_cap_gb"] / 1024,
        "Subscribed_TB": details["total_subscribed_cap_gb"] / 1024
    })

df = pd.DataFrame(records)
df.to_excel("powermax_capacity_report.xlsx", index=False)
print(df)
