# WAP to get the largest number, smallest num and sum of all from a list. 

#create empty list 

v = []

num= int(input('How many elements to put in List: '))

for n in range(num):

    element = int(input('Enter element '))

    v.append(element)

print("Maximum element in the list is :", max(v))

print("Minimum element in the list is :", min(v))
