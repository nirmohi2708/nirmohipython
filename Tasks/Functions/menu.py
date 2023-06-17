# WAP to create a menu using functions


print("================Welcome to TOPS Restaurant================")


print('''
     Sr.No. Item       Price   
     1      Pizza      90/-
     2      Burger     80/-
     3      Pani-puri  100/-
     4      Dosa       110/-
''')

def piz():
    def bur():
    def pani():
    def dos():

status=True:
while status:

choice=input("Enter your item :")
quant=int(input("Enter quantity :"))

if choice==pizza :
    print("Your item is Pizza")
    print("Quantity :",quant)
   
    if quant>1:
        A=("Total price :",quant*90)
    else:
         a=("Total price :",price=90)

elif choice==burger :
    print("Your item is Burger")
    print("Quantity :",quant)
   
    if quant>1:
        B=("Total price :",quant*80)
    else:
         b=("Total price :",price=80)

elif choice==pani-puri :
    print("Your item is Pani-puri")
    print("Quantity :",quant)
   
    if quant>1:
        C=("Total price :",quant*100)
    else:
         c=("Total price :",price=100)

elif choice==dosa :
    print("Your item is Dosa")
    print("Quantity :",quant)
   
    if quant>1:
        D=("Total price :",quant*110)
    else:
         d=("Total price :",price=110)

n=input("Do you want to continue ? [y/n]")
print("---------------------------------------------------------------------")
if n=='y' or 'Y' or'Yes':
    status=True
else:
    print("THANK YOU !!")

if choice==pizza:
    print("Total bill :",a)

    if quant>1:
        print("Total bill :",A)
    else:
        pass

elif choice==burger:
    print("Total bill :",b)

    if quant>1:
        print("Total bill :",A)
    else:
        pass

elif choice==pani-puri:
    print("Total bill :",c)

    if quant>1:
        print("Total bill :",C)
    else:
        pass

elif choice==dosa:
    print("Total bill :",d)

    if quant>1:
        print("Total bill :",D)
    else:
        pass

else:
    pass





    










#choice=int(input("Enter choice : "))




