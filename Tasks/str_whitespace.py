# WAP to identify the white spaces in the string entered by the user

v=input("Enter string :")

count=0

for i in range(0,len(v)):
    if v[i]==" ":
        count+=1

print("White spaces : ",count)
    

