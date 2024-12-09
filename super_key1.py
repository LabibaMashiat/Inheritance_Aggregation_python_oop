#Uing super() key we can access method and constructor of parents, not attribute
class A:
    def __init__(self,num):
        print("Inside Parent Constructor.")
        self.num=num
    def get_num(self):
        print("Number is= ",self.num)
class B(A):
    def get_num(self):
        print("Inside Class B")
        super().get_num()
        print("The value is = ",self.num)
obj1=B(100)
obj1.get_num()
   
