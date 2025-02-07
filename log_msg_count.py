logs = [
"INFO: Server started",
"ERROR: Connection failed",
"WARNING: Disk usage high",
"INFO: Task completed",
"ERROR: Timeout occurred"
]

log_count={}
sum = 0

for i in logs:
    log_dict=i.split(":")[0]
    #print(log_dict)
    if log_dict in log_count:
        log_count[log_dict] +=1
    else:
        log_count[log_dict] = 1
print(log_count)