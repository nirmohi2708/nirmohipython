# WAP to reverses a string if its length is a multiple of 4.

v=input("Enter the String :")
if len(v) % 4 == 0:
   print(''.join(reversed(v)))
else:
	print(v)
