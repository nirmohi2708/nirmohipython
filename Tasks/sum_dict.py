# WAP to do summation of elements of two dictionaries

v={'a':100,'b':10,'c':90}

n={'a':20,'b':30,'c':20}



# adding the values with common key
for key in n:
    if key in v:
        n[key] = n[key] + v[key]
    else:
        pass
		
print("The summation of elements of dict-v and dict-n is :",n)

