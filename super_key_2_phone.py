class Phone:
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
        print("Inside Phone Constructor")
class Smartphone(Phone):
    def __init__(self, price, brand, camera,op,memory):
        super().__init__(price, brand, camera) 
        self.op=op
        self.memory=memory 
        print("Inside Smartphone Constructor")
phn1=Smartphone(80000,"Samsung",13,"Android",8)
print(phn1.brand)
print(phn1.op)              
        