'''
Enter 10 number input from user
Count of even Numbers : 
Count of Odd Numbers :
Sum of Even numbers : 
Sumof Odd numbers :
'''

e=0
od=0

print("Enter 10 numbers :")

for i in range(1,11):
    num=int(input())
    if num%2==0:
        e+=1
    else:
        od+=1

#printing the total number of odd and even numbers 

ev=print("Total even numbers are :",e)
odd=print("Total odd numbers are :",od)

#adding the number of even numbers and number of odd numbers

sum=ev+odd
print("The sum of even and odd number is :",sum)


