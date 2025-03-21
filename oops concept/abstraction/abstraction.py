# from abc import ABC         # ABC will act as a parent class (functions are hidden)
# from abc import abstractmethod
# class Vehicle(ABC) :        # Vehicle is parent abstract class. (Should inherit ABC)
#     @abstractmethod         # Indicates Mandatory Implementation
#     def regno(self,r):
#         pass                # Abstract methods in a parent class serve as placeholders, requiring subclasses to define their functionality
#     @abstractmethod
#     def owner(self,o):
#         pass
#     @abstractmethod
#     def mileage(self,m):
#         pass
#     @abstractmethod
#     def fueltype(self,f):
#         pass
# class Car(Vehicle):
#     def sunroof(self):             # If we only call sunroof() an error will occur --> Can't instantiate abstract class Car
#         print('Car have sunroof')            # without an implementation for abstract methods 'fueltype', 'mileage', 'owner', 'regno'.
#     def regno(self,r):             # So must implement all functions that are decorated with @abstractmethod
#         print(r)                   # Define functionality of abstract method
#     def owner(self,o):
#         print(o)
#     def mileage(self,m):
#         print(m)
#     def fueltype(self,f):
#         print(f)
# obj=Car()
# obj.sunroof()
# obj.regno(4483)
# obj.owner('John')
# obj.mileage('30 MPG')
# obj.fueltype('Petrol')


# Q: Create an abstract class with abstract functions using arguments. atleast 2 child class required.
# atleast 3 abstractmethod required.
# A:
import math
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def face_perimeter(self,*args):
        pass
    @abstractmethod
    def face_area(self,*args):
        pass
    @abstractmethod
    def volume(self,*args):
        pass
class Cube(Shape):
    def surface_area(self,side):
        print('Surface Area=',(side**2)*6)    # side^2 * 6
    def face_perimeter(self,side):
        print('Face Perimeter=',side*4)
    def face_area(self,side):
        print('Face Area=',side**2)
    def volume(self,side):
        print('Volume=',side**3)
class Cylinder(Shape):
    def total_surface_area(self,radius,height):
        print('Total Surface Area=',2*math.pi*radius*(radius+height))
    def face_perimeter(self,radius):
        print('Face Perimeter=',2*math.pi*radius)
    def face_area(self,radius):
        print('Face Area=',math.pi*(radius**2))
    def volume(self,radius,height):
        print('Volume=',math.pi*(radius**2)*height)
cube=Cube()
cube.face_perimeter(3)
cube.face_area(3)
cube.surface_area(3)
cube.volume(3)

cylinder=Cylinder()
cylinder.face_perimeter(2)
cylinder.face_area(2)
cylinder.total_surface_area(2,4)
cylinder.volume(2,4)



