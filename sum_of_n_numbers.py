def sum_all_number(n):
    total = 0
    for i in range(1,n +1):
        total += i
    return total




n=int(input("Enter a valid integer number: "))

result=sum_all_number(n)

print(result)