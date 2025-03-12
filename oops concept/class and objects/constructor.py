# class Studnet:
#     def __init__(self,name,roll_no,department):
#         self.n=name
#         self.r=roll_no
#         self.d=department
#     def display(self):
#         print('Name:',self.n)
#         print('Roll No:',self.r)
#         print('Department:',self.d)
# # obj=Studnet()
# # obj.__init__('Gopika',26,'Statistics')     # this will result in an error
# # obj.display()
#
# obj=Studnet('Gopika',26,'Statisctics')
# obj.display()
#
# obj2=Studnet('Amal',53,'CS')
# obj2.display()
from idlelib.pyshell import PyShell


# Q: Create a class movie using constructor with static variables theatre name,location. attributes are movie,
# director,show_time,rating.create 3 objects
# A:
class Movie:
    theatre='PVR'
    location='Edappally'
    def __init__(self,movie,director,show_time,rating):
        self.m=movie
        self.d=director
        self.st=show_time
        self.r=rating

    def display(self):
        print('Theatre:',Movie.theatre)
        print('Location',Movie.location)
        print('Movie:',self.m)
        print('Director:',self.d)
        print('Show Time:',self.st)
        print('Rating:',self.r)
a=Movie('Interstellar','Cristopher Nolan','2.00 PM',9.7)
a.display()

b=Movie('Minnal Murali','Basil Joseph','10.00 AM',9.0)
b.display()

c=Movie('Drishyam','Jeethu Joseph','4.45 PM',9.2)
c.display()