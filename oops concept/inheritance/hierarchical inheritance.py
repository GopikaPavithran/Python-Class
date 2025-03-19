# class Parent:
#     def parentfun(self):
#         print('This is parent')
# class Child1(Parent):
#     def childfun1(self):
#         print('This is child 1')
# class Child2(Parent):
#     def childfun2(self):
#         print('This is child 2')
# c1=Child1()
# c1.parentfun()
# c1.childfun1()
#
# c2=Child2()
# c2.parentfun()
# c2.childfun2()


# Q: Write code for hierarchical inheritance
# Details(Parent) : name, age, gender, phone number                   # common attributes for each person
# Developer(Child) : company, department
# Doctor(Child) : hospital, specialization
# A:

#                     # without constructor
#
# class Details:
#     def det(self,name,age,gender,phone):
#         self.n=name
#         self.a=age
#         self.g=gender
#         self.p=phone
# class Developer(Details):
#     def dev(self,company,department):
#         self.c=company
#         self.d=department
#     def display_dev(self):
#         print('Name:',self.n)
#         print('Age:',self.a)
#         print('Gender:',self.g)
#         print('Phone:',self.p)
#         print('Company:',self.c)
#         print('Department:',self.d)
# class Doctor(Details):
#     def doc(self,hospital,specialization):
#         self.h=hospital
#         self.s=specialization
#     def dispaly_doc(self):
#         print('Name:',self.n)
#         print('Age:',self.a)
#         print('Gender:',self.g)
#         print('Phone:',self.p)
#         print('Hospital:',self.h)
#         print('Specialization:',self.s)
# a=Developer()
# a.det('Gopika Pavithran',22,'Female',726384933)
# a.dev('Luminar','Data Science')
# a.display_dev()
#
# b=Doctor()
# b.det('Walter',56,'Male',935907)
# b.doc('City Hospital','Cardiology')
# b.dispaly_doc()

                    # using constructor

class Details:
    def __init__(self,name,age,gender,phone):
        self.n=name
        self.a=age
        self.g=gender
        self.p=phone
class Developer(Details):
    def __init__(self,name,age,gender,phone,company,department):
        super().__init__(name,age,gender,phone)
        self.c=company
        self.d=department
    def display_dev(self):
        print('Name:',self.n)
        print('Age:',self.a)
        print('Gender:',self.g)
        print('Phone:',self.p)
        print('Company:',self.c)
        print('Department:',self.d)
class Doctor(Details):
    def __init__(self,name,age,gender,phone,hospital,specialization):
        super().__init__(name,age,gender,phone)
        self.h=hospital
        self.s=specialization
    def dispaly_doc(self):
        print('Name:',self.n)
        print('Age:',self.a)
        print('Gender:',self.g)
        print('Phone:',self.p)
        print('Hospital:',self.h)
        print('Specialization:',self.s)
a=Developer('Gopika',22,'F',123456753,'KPMG','Data Science')
a.display_dev()

b=Doctor('Skyler',43,'F',63942,'SHR','Gynecology')
b.dispaly_doc()
