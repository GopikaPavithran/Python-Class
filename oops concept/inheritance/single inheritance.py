 # class Parent:
#     def parentfun(self):
#         print('This is parent class')
# class Child(Parent):    # child class inherits functions of parent class
#     def childfun(self):
#         print('This is child class')
# obj=Child()    # creating object of child class allows access to functions from both the child and parent classes
# obj.parentfun()
# obj.childfun()


# # Q: Create a parent class team_leader with attributes team_leader_name,work_block_no,company_name.create child
# # class employee with attributes employee_name,id,post. create an employee object
# # A:
#           # without using constructor
#
# class TeamLeader:
#     def fun1(self,team_leader_name,work_block_no,company_name):
#         self.tln=team_leader_name
#         self.wbn=work_block_no
#         self.cn=company_name
# class Employee(TeamLeader):
#     def fun2(self,employee_name,id,post):
#         self.en=employee_name
#         self.id=id
#         self.p=post
#     def fun3(self):
#         print('Team Leader:',self.tln)
#         print('Work Block',self.wbn)
#         print('Company:',self.cn)
#         print('Employee:',self.en)
#         print('ID:',self.id)
#         print('Post',self.p)
# obj=Employee()
# obj.fun1('Anshya',3,'Luminar')
# obj.fun2('Gopika',43,'Data Scientist')
# obj.fun3()

#             # using constructor
#
# class TeamLeader:
#     def __init__(self,team_leader_name,work_block_no,company_name):
#         self.tln = team_leader_name
#         self.wbn=work_block_no
#         self.cn=company_name
# class Employee(TeamLeader):
#     def __init__(self,team_leader_name,work_block_no,company_name,employee_name,id,post):    # also pass arguments from parent class
#         super().__init__(team_leader_name,work_block_no,company_name)     # super() -  to access functionality from the superclass(parent class). also pass arguments of parent class exclude self
#         self.en=employee_name
#         self.id=id
#         self.p=post
#     def display(self):
#         print('Team Leader:',self.tln)
#         print('Work Block',self.wbn)
#         print('Company:',self.cn)
#         print('Employee:',self.en)
#         print('ID:',self.id)
#         print('Post',self.p)
# obj=Employee('Anshya',3,'Luminar','Gopika',2243,'Data Scientist')
# obj.display()


# Q: Using constructors create parent class doctor with attributes doctor_name,specialization and child class
# patient with attributes patient_name,token_number
# A:
class Doctor:
    def __init__(self,doctor_name,specialization):
        self.dn=doctor_name
        self.s=specialization
class Patient(Doctor):
    def __init__(self,doctor_name,specialization,patient_name,token_number):
        super().__init__(doctor_name,specialization)
        self.pn=patient_name
        self.tn=token_number
    def display(self):
        print('Doctor:',self.dn)
        print('Specialization:',self.s)
        print('Patient Name:',self.pn)
        print('Token Number:',self.tn)
obj=Patient('Dr.Radhakrishnan','Cardiology','Akhil',28)
obj.display()
