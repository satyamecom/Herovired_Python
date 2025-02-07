import re

def check_password_strength(password):
    if len(password) >=8 and re.search(r'[a-z]',password) and re.search(r'[A-Z]',password) and re.search(r'[0-9]',password) and re.search(r'[!@#$%^&*()]',password):
        print("Provided password fulfil the criteria:",True)
    else:
        print("Provided password fulfil the criteria:",False)
    return password


user_passw=input(str("Enter a password: "))
check_password_strength(user_passw)