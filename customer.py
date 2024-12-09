class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.address=address
        self.gender=gender
    def edit_profile(self,new_city ,new_pincode,new_state,new_name=None):
        if new_name is None:
            new_name=self.name
        
        self.name=new_name
        self.address.change_address(new_city,new_pincode,new_state)

class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    def change_address(self,new_city,new_pincode,new_state):
        self.city=new_city
        self.pincode=new_pincode
        self.state=new_state

add=Address("Kolkata",110,"WB")
cust1=Customer("Mahi","Female",add)
cust1.edit_profile("Mumbai",109,"IN")

print(cust1.name)