status=True
while status:
    sum=0
    for i in range(1,6):
        n=int(input("Enter number"))
        sum+=n

        print("The sum is :",sum)

        choice=input("Would you like to continue ? [y/n]")

    if choice=='y' or choice=="Yes":
        status=True
    else:
        status=False
