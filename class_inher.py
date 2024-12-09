class B:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
class A(B):
    def __init__(self, val,num):
        self.__val=val
        self.num=num
        
    def get_val(self):
        return self.__val
obj1=A(100,10)
print(obj1.get_val())
# print(obj1.get_num())--> got error