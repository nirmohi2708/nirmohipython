# WAP to check if the entered number is positive, negative or zero.



value=int(input("Enter number :"))

if value>=0: #number greater than zero will be positive  
    if value==0: #exact zero has to be printed zero
        print("The number entered is zero")
    else:
        print("The number entered is positive number")

else:  #number lesser than zero will be negative.
    print("The entered number is negative")
