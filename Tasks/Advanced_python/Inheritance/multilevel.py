#Multi-level Inheritance

class A:
    def displayA(self):
        print("Class A")

class B(A):
    def displayB(self):
        print("Class B")

class C(B):
    def displayC(self):
        print("Class C")

c1= C()

c1.displayA()
c1.displayB()
c1.displayC()
