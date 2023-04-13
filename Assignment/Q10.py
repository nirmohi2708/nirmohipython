# WAP program that will return true if the two given integer values are equal or their sum or difference is 5.

#taking value from the user

v1=int(input("Enter value 1 :"))
v2=int(input("Enter value 2 :"))

# giving condition

if v1==v2 or v1-v2 ==5 or v1+v2==5:
    print("True ")
else:
    print("Fale")
