import yaml

apps = [
{"name": "nginx", "replicas": 3, "image": "nginx:latest"},
{"name": "redis", "replicas": 2, "image": "redis:latest"}
]

emlist=[]
for i in apps:
    deployment={"apiVersion" : "apps/v1",
        "Kind" : "Deployment",
        "metadata": {"name" : i["name"]},
        "spec" : {"replicas": i["replicas"],"selector": {"matchLabels": {"app":i["name"]}},"template":{"metadata":{"labels":{"app":i["name"]}},"spec":{"containers":{"-name":i["name"],"image":i["image"]}}}}
    }


    emlist.append(deployment)  # Add each deployment to the list

# Write all configurations to the YAML file
with open("person_data.yaml", "w") as file:
    yaml.dump_all(emlist, file, sort_keys=False)

print("YAML file saved.")