# WAP to replace last value of tuples in a list.

v=(1,2,3,4,5,6,7)


for t in v:
    print(t[:-1] + (10,))
