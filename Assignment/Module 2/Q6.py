# WAP to swap two numbers with temp variable and without temp variable


# with using third variable 

'''
a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))
temp=c

c=a
a=b
b=a

print("The updated value of a is",a)
print("The updated value of b is",b)

'''
# without using third variable

a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))

a=a+b
b=a-b
a=a-b

print("The updated value of a is",a)
print("The updated value of b is",b)


