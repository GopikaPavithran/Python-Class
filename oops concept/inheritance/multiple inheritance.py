# class A:
#     def funA(self):
#         print('Parent A')
# class B:
#     def funB(self):
#         print('Parent B')
# class C(A,B):
#     def funC(self):
#         print('Child C')
# obj=C()
# obj.funA()
# obj.funB()
# obj.funC()


# # Q: Create parent class hospital with attributes hospital_name,location another parent class doctor with
# # attributes doctor_name,specialization and child class patient with attributes patient_name,token_number
# # A:
#                 # without using constructor
#
# class Hospital:
#     def hos(self,hospital_name,location):
#         self.hn=hospital_name
#         self.l=location
# class Doctor:
#     def doc(self,doctor_name,specialization):
#         self.dn=doctor_name
#         self.s=specialization
# class Patient(Hospital,Doctor):
#     def pat(self,patient_name,token_number):
#         self.pn=patient_name
#         self.tn=token_number
#     def display(self):
#         print('Hospital:',self.hn)
#         print('Location:',self.l)
#         print('Doctor:',self.dn)
#         print('Specialization:',self.s)
#         print('Patient Name:',self.pn)
#         print('Token Number:',self.tn)
# obj=Patient()
# obj.hos('KAH','Cheruvathur')
# obj.doc('Muhammad Ali','Neurology')
# obj.pat('Alex',12)
# obj.display()

#                 # using constructor
#
# class Hospital:
#     def __init__(self,hospital_name,location):
#         self.hn=hospital_name
#         self.l=location
# class Doctor:
#     def __init__(self,doctor_name,specialization):
#         self.dn=doctor_name
#         self.s=specialization
# class Patient(Hospital,Doctor):
#     def __init__(self,hospital_name,location,doctor_name,specialization,patient_name,token_number):      # also pass arguments from parent class
#         Hospital.__init__(self,hospital_name,location)        # to access functionality from more than one parent use parent class name(class name method) instead of super(). also pass arguments of parent class including self
#         Doctor.__init__(self,doctor_name,specialization)
#         self.pn=patient_name
#         self.tn=token_number
#     def display(self):
#         print('Hospital:',self.hn)
#         print('Location:',self.l)
#         print('Doctor:',self.dn)
#         print('Specialization:',self.s)
#         print('Patient Name:',self.pn)
#         print('Token Number:',self.tn)
# obj=Patient('KAH','Cheruvathur','Muhammad Ali','Neurology','Alex',12)
# obj.display()


# Q: Using constructors create class for multiple inheritance and create 3 objects
# A:
class Library:
    def __init__(self,library_name,location):
        self.ln=library_name
        self.l=location
class Book:
    def __init__(self,title,book_number,author):
        self.t=title
        self.a=author
        self.bn=book_number
class Member(Library,Book):
    def __init__(self,library_name,location,title,book_number,author,member_name,borrow_date,return_date):
        Library.__init__(self,library_name,location)
        Book.__init__(self,title,book_number,author)
        self.mn=member_name
        self.bd=borrow_date
        self.rd=return_date
    def display(self):
        print('Library:',self.ln)
        print('Location:',self.l)
        print('Book:',self.t)
        print('Author:',self.a)
        print('Book Number:',self.bn)
        print('Member Name:',self.mn)
        print('Borrow Date:',self.bd)
        print('Return Date:',self.rd)
a=Member('Azheekkodan Smaraka Vayanashala & Grandhalayam','Aminhikode','Francis Ittycora',
         2364,'T D Ramakrishnan','Gopika Pavithran','20-01-2025','18-03-2025')
a.display()

b=Member('M K Nair Library','Padanekkad','Harry Potter and The Order of Phoenix',5195,
         'J K Rowling','Gopika Pavithran','05-02-2023','04-03-2023')
b.display()

c=Member('G H S S Kuttamath Library','Kuttamath','Paavangal',826,'Victor Hugo',
         'Gopika Pavithran','16-08-2014','23-08-2014')
c.display()