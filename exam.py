# # 1. Create a class Vehicle without any variables and methods
# # A:
# class Vehicle:
#     pass


# # 2: Create a parent class Vehicle with child classes Bus,Car,Bike with any attributes. the child classes should
# # access the properties and behaviour of parent class. then create a bus object , a car object and a bike object
# # (use constructor)
# # A:
# class Vehicle:
#     def __init__(self,brand,model,year):
#         self.b=brand
#         self.m=model
#         self.y=year
# class Bus(Vehicle):
#     def __init__(self,brand,model,year,mileage):
#         super().__init__(brand,model,year)
#         self.mil=mileage
#     def bus_display(self):
#         print('Brand:',self.b)
#         print('Model:',self.m)
#         print('Year:',self.y)
#         print('Mileage:',self.mil)
# class Car(Vehicle):
#     def __init__(self,brand,model,year,fuel_type):
#         super().__init__(brand,model,year)
#         self.ft=fuel_type
#     def car_display(self):
#         print('Brand:',self.b)
#         print('Model:',self.m)
#         print('Year:',self.y)
#         print('Fuel Type:',self.ft)
# class Bike(Vehicle):
#     def __init__(self,brand,model,year,price):
#         super().__init__(brand,model,year)
#         self.p=price
#     def bike_display(self):
#         print('Brand:',self.b)
#         print('Model:',self.m)
#         print('Year:',self.y)
#         print('Price:',self.p)
# a=Bus('Volvo','B8R',2023,8.5)
# a.bus_display()
#
# b=Bike('Honda','CBR500R',2021,500000)
# b.bike_display()
#
# c=Car('Toyota','Carmy',2022,'Gasoline')
# c.car_display()


# # 3. What does super() do in python?
# # A:
# super() is a method to access the constructor of parent class


# # 4. What is member function? Give another name for member function.
# # A:
# Member function is function that is associated with a specific class.
# Method is another name for a member function.


# # 5. Explain difference between multiple inheritance and single inheritance with example code.
# # A:
# In single inheritance, a class can inherit from only one parent class.
# eg:
# class Parent:
#     def parentfun(self):
#         print('Parent')
# class Child(Parent):
#     def childfun(self):
#         print('Child')
# obj=Child()
# obj.childfun()
# obj.parentfun()
#
# In multiple inheritance, a class can inherit from more than one parent class.
# eg:
# class Parent1:
#     def parentfun1(self):
#         print('Parent 1')
# class Parent2:
#     def parentfun2(self):
#         print('Parent 2')
# class Child(Parent1,Parent2):
#     def childfun(self):
#         print('Child')
# obj=Child()
# obj.parentfun1()
# obj.parentfun2()
# obj.childfun()


# # 6. What is static variable? Give an example of static variable in inheritance
# # A:
# Static variables or class variables that are share among all objects of a class. It is defined inside a class
# and outside a method. It is useful when we want all objects of a class to share the same value
#
# class Student:
#     college='Nehru Arts and Science College'
#     def student_details(self,name,reg_no):
#         self.n=name
#         self.rn=reg_no
# class Mark(Student):
#     def marks(self,maths,cs,statistics):
#         self.m=maths
#         self.c=cs
#         self.s=statistics
#     def print_mark(self):
#         print('College:',Student.college)
#         print('Name:',self.n)
#         print('Register No:',self.rn)
#         print('Marks','\n----')
#         print('Maths:',self.m)
#         print('Computer Science:',self.c)
#         print('Statistics:',self.s)
# obj=Mark()
# obj.student_details('Gopika Pavithran','NA20CSTR28')
# obj.marks(100,100,100)
# obj.print_mark()
