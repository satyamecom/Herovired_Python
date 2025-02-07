logs = [
"ERROR: Disk full1",
"INFO: Backup started",
"ERROR: Disk full",
# "WARNING: Memory usage high",
"ERROR: Connection timeout",
"ERROR: Connection timeout",
"ERROR: Connection timeout",
"ERROR: Disk full"
]

# sum =0
# comm=0
# for i in logs:
#     x=i.split(":")
#     if x[0] == "ERROR":
#         #print(x)n
#         sum = sum + 1
# print("Total error count is :",sum)


# mdict={}
# sum=0
# for i in logs:
#     emdict=i.split(":")[1]
#     # print(emdict)
#     if emdict in mdict:
#         mdict[emdict]+=1
#     else:
#         mdict[emdict]=1
#     print("mdict",mdict)

# max_item = max(mdict.items(),key=lambda x:x[1])
# print(max_item[0])

mdict={}
count = 0
max_oc = 0
max_oc_str = ''
# breakpoint()
for i in logs:
    edict=i.split(":")
    if edict[0] == 'ERROR':
        count+=1
        if edict[1] in mdict:
            mdict[edict[1]]+=1
        else:
            mdict[edict[1]]=1
        if mdict.get(edict[1]) > max_oc:
            max_oc_str = edict[1]
            max_oc = mdict[edict[1]]
    # if edict in mdict:
    #     mdict[edict] +=1
    #     #print(mdict)
    # else:
    #     mdict[edict] =1
print(f"Total Errors : {count}")
print(max_oc_str)

# print(f"Occured error is {sorted(mdict,key=mdict[1])}")








