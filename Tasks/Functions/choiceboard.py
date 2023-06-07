# WAP for choice board

board='''
    =====choice Board=====

        1. Addition
        2. Multiplication
        3. Modulous
        4. Division
        5. Substraction

'''


def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def mod(a,b):
    return a%b

def div(a,b):
    return a/b

def sub(a,b):
    return a-b


status=True
while status:
    
    print(board)

    choice=int(input("Enter choice : "))

    n1=int(input("Enter num 1: "))
    n2=int(input("Enter num 2: "))

    if choice==1:
        print("Addition : ",add(n1,n2))
    elif choice==2:
        print("Multiplication : ",mul(n1,n2))
    elif choice==3:
        print("Mod : ",mod(n1,n2))
    elif choice==4:
        print("division : ",div(n1,n2))
    elif choice==5:
        print("Substraction : ",sub(n1,n2))
    else:
        print("Invalid Choice !!")


    n=input("Do you want to continue ?[y/n]")
    if n=='y' or n=='Y'or n=='yes':
        status=True
    else:
        status=False
