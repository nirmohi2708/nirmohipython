# WAP to insert a string in the middle of a string.

v = input("Enter main string: ")  #taking string1 as input

n = input("Enter the string to be inserted: ") #taking string2 as input

position = int(input("Enter the position in which string should be inserted: ")) #input position

v = v[:position]+n+v[position:] #inserting string2 between string1 at required position

print(v) #printing the output
