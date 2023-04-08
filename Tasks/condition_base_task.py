#Condition based task 

#Getting information from user

name=input("Please enter your name here : ")

age=int(input("Please enter your age here : "))

amount=int(input("Please enter your total amount here : "))

#Giving condition for discount eligibility




if amount>=5000:
    if age<=18 or age<=30:
        d1=20
        print("The discount percent you get is 20%")
        discount=d1/amount*100
    if age>30 or age<=50:
        d2=30
        print("The discount percent you get is 30%")
        discount=d2/amount*100
    if age>50:
        d3=50
        print("The discount percent you get is 50%")
        discount=d3/amount*100
else:
     print("Sorry you're not eligible for discount")


#getting the final outcome printed 

print("\n=======INVOICE=======\n")
print("Name :",name)
print("Age :",age)
print("Total amount :",amount)
print("Discount amount",discount)
print("Total payment amount:",amount-discount)





