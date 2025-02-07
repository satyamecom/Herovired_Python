def compund_interest(pr_amt,rate_int,time_yer):
    comp_int=pr_amt*(1+(rate_int/100))**time_yer
    amount=comp_int + pr_amt
    return comp_int,amount


pr_amt=int(input("mention the principal amount: "))
rate_int=float(input("mention the rate of interest :"))
time_yer=int(input("mention the year :"))


compound,total_amt=compund_interest(pr_amt,rate_int,time_yer)
print("Compund interest would be :",compound)
print("Total amount would be :",total_amt)
