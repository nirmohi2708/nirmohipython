#Multiple Inheritance

class Mom:
    def displayM(self):
        print("MOM Class")

class Dad:
    def displayD(self):
        print("DAD Class")

class Child(Mom,Dad):
    def displayC(self):
        print("Child Class")

c1 = Child()

c1.displayM()
c1.displayD()
c1.displayC()
