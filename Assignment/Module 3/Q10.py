# WAP that takes two lists and returns true if they have at least one common member.

v=input("Enter list : ")
n=input("Enter list 2 : ")

for i in v:
    for i in n:
        if v==n:
            result=True
        else:
            result=False

print("Common data : ")
