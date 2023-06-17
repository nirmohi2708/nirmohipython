#Single-level Inheritance

class A:
    def displayA(self):
        print("Class A")

class B(A):
    def displayB(self):
        print("Class B")



b1= B()

b1.displayA()
b1.displayB()
