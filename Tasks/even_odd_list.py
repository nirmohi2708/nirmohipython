# WAP to take 10 user input elements and put them in two different list on the bases of odd number and even number

even=[]

odd=[]



for n in range(1,11):
    v=int(input("Enter any value :"))


    
    if v%2==0:
        v.append(even)
    else:
        v.append(odd)

print("Even",even)

print("odd",odd)
