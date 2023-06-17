class parent:
    def displayA(self):
        print("Class A")

class B(parent):
    def displayB(n):
        print("Class B")

class C(parent):
    def displayC(v):
        print("Class C")

class D(parent):
    def displayD(v):
        print("Class D")

class E(B):
    def displayE(v):
        print("Class E")

class F(D):
    def displayF(v):
        print("Class F")

class G(D):
    def displayG(v):
        print("Class G")

class H(D):
    def displayH(v):
        print("Class H")


obj1 = B()
obj2 = E()
obj3 = C()
obj4 = D()
obj5 = F()
obj6 = G()
obj7 = H()





obj1.displayA()
obj2.displayB()
obj3.displayA()
obj4.displayA()
obj5.displayD()
obj6.displayD()
obj7.displayD()






