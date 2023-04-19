# WAP to find the second smallest number in a list.

v = [] 
n = int(input("Enter the number of elements: "))
for i in range(1, n+1): 
    s = int(input("Enter the elements: ")) 
    v.append(s) 
v.sort() 

print("The sorted list: ", v) 
print("The second smallest value of this list: ",v[1])
