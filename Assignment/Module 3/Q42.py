# WAP to combine two dictionary adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300})



v={'a':100,'b':10,'c':90}

n={'a':20,'b':30,'c':20}



# adding the values with common key
for key in n:
    if key in v:
        n[key] = n[key] + v[key]
    else:
        pass
		
print("The summation of elements of dict-v and dict-n is :",n)

