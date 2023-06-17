# hybrid inheritance


class parent:
	def func1(self):
		print("Parent class.")


class Child_a(parent):
	def func2(self):
		print("Child a ")


class Child_b(parent):
	def func3(self):
		print("Child  b ")


class child_c(Child_a, parent):
	def func4(self):
		print("Child c")


obj = child_c()
obj.func1()
obj.func2()
