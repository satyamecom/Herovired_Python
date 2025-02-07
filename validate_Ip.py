
ip_list=["192.168.1.1","256.100.50.25"]

for i in ip_list:
    ip = i.split('.')
    for j in ip:
        if int(j)<0 or int(j)>255:
            print(f"{i} is invalid")
            break
    print(f'{i} is valid')
        # spl1in=int(i.split(".")[0][0])
        # spl2in=int(i.split(".")[1][0])
        # spl3in=int(i.split(".")[2][0])
        # spl4in=int(i.split(".")[3][0])

        # spl1=int(i.split(".")[0])
        # spl2=int(i.split(".")[1])
        # spl3=int(i.split(".")[2])
        # spl4=int(i.split(".")[3])
        
        # if spl1in != 0 and spl1 <= 255 and spl2in !=0 and spl2 <=255 and spl3in !=0 and spl3 and spl4in !=0 and spl4:
        #     print(i,"valid")
        # else:
        #     print(i,"invalid")
        
# for i in ip_list:
#     four_oct=len(i.split("."))
#     if four_oct < 4:
#         print(i,"invalid IP")
#     else:
#         print(i,"valid IP")
 
    




