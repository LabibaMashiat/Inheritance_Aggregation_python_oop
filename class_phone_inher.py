class Phone:
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price=price
        self.__brand=brand
        self.camera=camera
class Smartphone(Phone):
    pass
phn1=Smartphone(3000,"Apple",13)
# print(phn1.__brand)--->got an error that attribute does not exist
# private attribute can not be inheritated
#Method Overriding-->if same name attribute or function exists in both parent and child class thyen child will call its own method,not the method of parents
# Polymorphism-->1)Method Overriding 2)Method Overloading 3)Operator Overloading


        
