status=True
while status:
    name=input("Enter name :")
    print("Your name is :",name)

    choice=input("Would you like to continue ? [y/n]")

    if choice=='y' or choice=="Yes":
        status=True
    else:
        status=False
