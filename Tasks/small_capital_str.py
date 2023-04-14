# WAP to take input string from user and find count of capital and small letters

v=input("Enter string : ")

lower=0
capital=0

for i in v:
    if i.islower():
        lower+=1
    else:
        capital+=1

print("The number of small letters in the string are ",lower)
print("The number of capital letters in the string are ",capital)
