disk_usage = {"server1": 70, "server2": 85, "server3": 65, "server4": 90}

#print(len(disk_usage))

#for i in len(disk_usage):

for i,x in disk_usage.items():
    #print(i,x)
    if x > 80:
        print("High disk usage on",i,x)