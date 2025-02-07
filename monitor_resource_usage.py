servers = [
{"name": "server1", "cpu": 75, "memory": 65},
{"name": "server2", "cpu": 85, "memory": 50},
{"name": "server3", "cpu": 60, "memory": 80},
{"name": "server4", "cpu": 50, "memory": 60}
]

healthy=[]
unhealthy=[]
for i in servers:
    #print(i)
    if i["cpu"] < 80 and i["memory"] < 70:
        #print("Healthy",i["name"])
        x=i["name"]
        healthy.append(x)
        #print("Healthy :",healthy)
    else:
        #print("Unhealthy",i["name"])
        y=i["name"]
        unhealthy.append(y)
        #print("Unhealthy:",unhealthy)
print("Healthy :",healthy)
print("Unhealthy:",unhealthy)