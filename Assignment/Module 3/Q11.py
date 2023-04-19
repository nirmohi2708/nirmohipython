# WAP that takes a list and returns a new list with unique elements of the first list.

v=input("Enter list : ")
n = []
for a in v:
    if a not in n:
      n.append(a)
  

print("unique_list",n) 

