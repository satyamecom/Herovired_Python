servers = [
{"name": "web1", "status": "active"},
{"name": "db1", "status": "inactive"},
{"name": "app1", "status": "active"}
]

for i in servers:
    if i["status"] == "inactive":
        print("Skipping backup for ",i["name"])
    else:
        print("Backing UP for ",i["name"])
        