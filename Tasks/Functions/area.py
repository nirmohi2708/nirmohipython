# Wap to find area of shapes using functions

board='''
        =============Area Finder=============

	1. Circle
	2. Triangle
	3. Rectangle 

 '''

print(board)

def circle(a,b):
    return pi*r*r
def triangle(a,b):
    return 1/2*h*b
def rectangle(a,b):
    return 1/2*h*b

choice=int(input("Enter choice number : "))

  

if choice==1:
    r=int(input("Enter the radius value : "))
    pi=3.14
    #cir_ar=pi*r*r
    print("The area of the circle is :",circle(r,pi))

elif choice==2:
    h=int(input("Enter the height :"))
    b=int(input("Enter the base :"))
    #tri_ar=1/2*h*b
    print("The area of the triangle is :",triangle(h,b))

elif choice==3:
    l=int(input("Enter the length :"))
    w=int(input("Enter the width :"))
    #rec_ar=l*b
    print("The area of the rectangle is :",rectangle(l,b))

else:
    print("Invalid choice !!!")

        
        











