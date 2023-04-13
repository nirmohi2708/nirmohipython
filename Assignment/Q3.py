#Write a Python program to get the Fibonacci series of given range.


terms = int(input("How many terms : "))

# first two terms
v1,v2 = 0, 1
count = 0

# check if the number of terms is valid
if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(v1)
# print fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(v1)
       nth = v1 + v2
       # update values
       v1 = v2
       v2 = nth
       count += 1

