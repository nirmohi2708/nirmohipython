# WAP to Count How many digits are there in a string

v=input("Enter string with numbers :")

digit=0

for ch in v :
    if ch.isdigit():
        digit=digit+1
print("No of digits is : ",digit)
