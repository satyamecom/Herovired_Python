services = [
{"name": "nginx", "status": "running"},
{"name": "mysql", "status": "stopped"},
{"name": "redis", "status": "running"}
]


#service_dict= dict(services)


for i in services:
    #print(i)
    if i["status"] != "running":
        print(i)