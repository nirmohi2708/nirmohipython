# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

#taking value from the user 
v1=int(input("Enter a value :"))
v2=int(input("Enter a value :"))
v3=int(input("Enter a value :"))

# Giving condition 

if v1==v2 or v2==v3 or v3==v1:
    print(sum=0)
else:
    total=v1+v2+v3
    sum=total

#Getting the output printed

    print("The total of the value is : ",sum)


