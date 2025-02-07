servers = [
{"hostname": "web1", "ip": "192.168.1.101"},
{"hostname": "db1", "ip": "192.168.1.102"}
]

# print(type(servers))
# conv=dict(servers)
# print(type(conv))
# print(conv.items())
# print(conv.values())

for i in servers:
    server = {}
    server["Listen"]=80
    server["Server Name"] = i.get("hostname")
    server["Address"] = i.get("ip")
    print("server= ",server)