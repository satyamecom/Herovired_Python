print("Hi There...!! Login to server")
#passwd=input("Enter a password: ")


exusername="satyam.v@example.com"
expassd="VermaSatyam123"
while True:
    username=input("Enter a username to login: ")
    if exusername == username:
        print("You have entered a correct username")
        while True:
            passwd=input("Enter a password: ")
            if expassd == passwd:
                print("Password matched successfully...!!!")
                break
        break
    else:
        print("Username not found, Please try again")
