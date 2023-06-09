# WAP to take input from user and print the details


    def input(self):
        self.name=input("Enter Name : ")
        self.age=int(input("Enter age : "))

    def display(self):
        print("your Name : ",self.name)
        print("Your Age : ",self.age)
    

p1= Person()

p1.input()
p1.display()
