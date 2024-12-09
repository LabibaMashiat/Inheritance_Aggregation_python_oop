# Python-->technically no method overloading,but we can do it.
class Geometry:
    def area(self,r,b=0):
        if b==0:

            print("Circle= ", 3.14*r*r)
        else:
            print("Rectangle= ",r*b)
circ=Geometry()
circ.area(4)      
circ.area(2,3)      