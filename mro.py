# Method Resolution Order
class Grandparent:
    def function(self):
        print("This is grandparent function")
class Parent(Grandparent):
    def function(self):
        print("This is parent function")
class Child(Parent):
    pass
obj1=Child()
obj1.function()
