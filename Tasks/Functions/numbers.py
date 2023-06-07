# WAP to write numbers from 1-10 without using loop

# using recursive function to print numbers

def num(a):
    if(a>0):
        num(a-1)
        print(a)
a=10
num(a)
