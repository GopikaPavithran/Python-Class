# class Laptop:
#
#     # for setting values
#     def setvalue(self,name,model,year,ram,processor,price):
#         self.nm=name       #instance variable - to make the data public or to access the data outside the fuction
#         self.mod=model
#         self.y=year
#         self.r=ram
#         self.pro=processor
#         self.pr=price
#
#     # for display the objects
#
#     def printvalue(self):
#         print('Laptop Name:',self.nm)     # accessing instance variable outside setvalue function
#         print('Model:',self.mod)
#         print('Year:',self.y)
#         print('Ram:',self.r)
#         print('Processor:',self.pro)
#         print('Price:',self.pr)
#
# obj1=Laptop()
# obj1.setvalue('Lenovo','ThinkPad T480',2018,'16GB','Intel Core i5',35000)
# obj1.printvalue()
#
# obj2=Laptop()
# obj2.setvalue('Dell','Latitude 5490',2024,'16GB','Intel Core i7',85000)
# obj2.printvalue()

# # each object should have its own reference variable so that it can store and access unique data.
# # using only one reference variable for multiple objects, it will overwrite the previous object reference,
# #                                                                  and lose access to the earlier objects.


# # Q: Create a class car with attributes company_name,model,fuel_type,color,transmission,price. for setting
# # the value create setvalue() for display the value create display() and create 3 objects
# # A:
class car:
    def setvalue(self,company_name,model,fuel_type,color,transmission,price):
        self.cn=company_name
        self.m=model
        self.ft=fuel_type
        self.c=color
        self.t=transmission
        self.p=price
    def display(self):
        print('Company Name:',self.cn)
        print('Model:',self.m)
        print('Fuel Type:',self.ft)
        print('Color:',self.c)
        print('Transmission:',self.t)
        print('Price:',self.p)
a=car()
a.setvalue('Toyota','Corolla','Petrol','White','Automatic','$25,000')
a.display()

b=car()
b.setvalue('Honda','Civic','Diesel','Black','Manual','$27,500')
b.display()

c=car()
c.setvalue('Tesla','Model 3','Electric','Red','Automatic','$40,000')
c.display()