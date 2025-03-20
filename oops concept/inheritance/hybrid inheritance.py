# class Parent:
#     def parentfun(self):
#         print('Parent')
# class Derived1(Parent):
#     def derivedfun1(self):
#         print('Derived 1')
# class Derived2(Parent):
#     def derivedfun2(self):
#         print('Derived 2')
# class Derived3(Derived1,Derived2):
#     def derivedfun3(self):
#         print('Derived 3')
# obj=Derived3()
# obj.derivedfun3()
# obj.derivedfun2()
# obj.derivedfun1()
# obj.parentfun()


# # Q: Write code for hybrid inheritance
# # University(Parent) : university name
# # College(Derived from University) : college name, location
# # Branch(Derived from University) : branch name
# # Student(Derived from College and Branch) : name, register number
# # A:
#
#                               # without using constructor
#
# class University:
#     def univ(self,u_name):
#         self.un=u_name
# class College(University):
#     def coll(self,c_name,location):
#         self.cn=c_name
#         self.l=location
#     def coll_display(self):
#         print('University:',self.un)
#         print('College:',self.cn)
#         print('Location',self.l)
# class Branch(University):
#     def bran(self,b_name):
#         self.bn=b_name
#     def bran_display(self):
#         print('University:',self.un)
#         print('Branch:',self.bn)
# class Student(College,Branch):
#     def stud(self,name,reg_no):
#         self.sn=name
#         self.rn=reg_no
#     def stud_display(self):
#         print('University:', self.un)
#         print('College:', self.cn)
#         print('Location', self.l)
#         print('Branch:', self.bn)
#         print('Student Name:',self.sn)
#         print('Register No:',self.rn)
# obj=Student()
# obj.univ('Kannur University')
# obj.coll('NASC','Kanhangad')
# obj.coll_display()
# obj.bran('Statistics')
# obj.bran_display()
# obj.stud('Regin',345)
# obj.stud_display()

                      # using constructor

class University:
    def __init__(self,u_name):
        self.un=u_name
class College(University):
    def __init__(self,u_name,c_name,location):
        University.__init__(self,u_name)
        self.cn=c_name
        self.l=location
    def coll_display(self):
        print('University:',self.un)
        print('College:',self.cn)
        print('Location',self.l)
class Branch(University):
    def __init__(self,u_name,b_name):
        University.__init__(self,u_name)
        self.bn=b_name
    def bran_display(self):
        print('University:',self.un)
        print('Branch',self.bn)
class Student(College,Branch):
    def __init__(self,u_name,c_name,location,b_name,name,reg_no):
        College.__init__(self,u_name,c_name,location)
        Branch.__init__(self,u_name,b_name)
        self.sn=name
        self.rn=reg_no
    def stud_display(self):
        print('University:', self.un)
        print('College:', self.cn)
        print('Location', self.l)
        print('Branch:', self.bn)
        print('Student Name:',self.sn)
        print('Register No:',self.rn)
obj=Student('Kannur University','NASC','Kanhangad','Chemistry','Athul','NA21CMST21')
obj.coll_display()
obj.bran_display()
obj.stud_display()