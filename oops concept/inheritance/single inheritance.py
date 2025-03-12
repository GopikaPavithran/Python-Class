# class Parent:
#     def parentfun(self):
#         print('This is parent class')
# class Child(Parent):    # child class inherits functions of parent class
#     def childfun(self):
#         print('This is child class')
# obj=Child()    # creating object of child class allows access to functions from both the child and parent classes
# obj.parentfun()
# obj.childfun()


# Q: Create a parent class team_leader with attributes team_leader_name,work_block_no,company_name.create child
# class employee with attributes employee_name,id,post. create an employee object
# A:
class TeamLeader:
    def fun1(self,team_leader_name,work_block_no,company_name):
        self.tln=team_leader_name
        self.wbn=work_block_no
        self.cn=company_name
    def fun2(self):
        print('Team Leader:',self.tln)
        print('Work Block',self.wbn)
        print('Company:',self.cn)
class Employee(TeamLeader):
    def fun3(self,employee_name,id,post):
        self.en=employee_name
        self.id=id
        self.p=post
    def fun4(self):
        print('Employee:',self.en)
        print('ID:',self.id)
        print('Post',self.p)
obj=Employee()
obj.fun1('Anshya',3,'Luminar')
obj.fun2()
obj.fun3('Gopika',43,'Data Scientist')
obj.fun4()