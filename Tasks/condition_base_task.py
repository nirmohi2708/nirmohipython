#Condition based task 

#Getting information from user

name=input("Please enter your name here : ")

age=int(input("Please enter your age here : "))

amount=int(input("Please enter your total amount here : "))

#Giving condition for discount eligibility

discount=0


if amount>=5000:
    if age>=18 and age<=30:
        d1=20
        print("The discount percent you get is 20%")
        discount=amount*d1/100
    elif age>30 and age<=50:
        d2=30
        print("The discount percent you get is 30%")
        discount=amount*d2/100
    elif age>50:
        d3=50
        print("The discount percent you get is 50%")
        discount=amount*d3/100
    else:
        print("As per the age Not Eligible !!!")
else:
     print("Sorry you're not eligible for discount")


#getting the final outcome printed 

print("\n=======INVOICE=======\n")
print("Name :",name)
print("Age :",age)
print("Total amount :",amount)
print("Discount amount :",discount)
print("Total payment amount:",amount-discount)





