# WAP to get unique values from a list

v=input("Enter list : ")

n = set(v) 
print("The unique elements of the input list using set():\n") 
t = (list(n))
 
for item in t: 
    print(item)
