# WAP to count the number of characters (character frequency) in a string

# taking user input

v=input("Enter the String: ")
n={}
# providing condition

for i in v:
    if i in n:
        n[i]+=1
    else:
        n[i]=1
print(n)
