# WAP to register in a travel agency website

# printing the objects in a variable 
options=("""
======= WELCOME TO TRAVEL AGENCY=======

OUR POPULAR DESTINATIONS :

1  Gujarat
2  Baroda
3  Mumbai
4  Kerela
5  Rajasthan
6  J&K
7  Arunachal Pradesh
8  Goa
9  Punjab
10 Manali
""")

# getting the variable info printed 
print(options)


# applying condition for registration 
n=input("""Do you want to register ?
[y/n]

""")
if n=='n':
    print("Thank you for you visit !!")
else:
    print("====== SIGN UP PLEASE !!!!! ======")
        
# creating a class and function for registration
class Register:
    def __init__(self):
# globalizing the variable in order to use it in further code
        global e
        global p
# taking info for registration 
        e=input("Enter email :")
        p=input("Enter password :")
        c=input("Enter confirm password :")
# applying condition for successful registation
        if p==c:
            print("Registration Successful")
        else:
            print("Password and confirm password are not same please check. ")

# creating object
# no need for calling object as dunder method/magic method is used 
reg=Register()


# creating second class for login process
print("===== LOGIN =====")
            
class Login:
    def login(self):
# taking info for login process
        le=input("Enter email :")
        lp=input("Enter password :")
# applying conditon for confirming whether both the details of sign up and login are same 
        if lp==p and le==e:
            print("Login Successful !!")
        else:
            print("Access Denied !! ")
# creating object and calling class 
log=Login()

log.login()
        





