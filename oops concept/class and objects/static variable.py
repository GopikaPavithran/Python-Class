# class Employee:
#     company_name='TCS'       # static variable
#     def setval(self,name,id,salary,designation):
#         self.n=name
#         self.i=id
#         self.s=salary
#         self.d=designation
#     def display(self):
#         print('Company Name:',Employee.company_name)   # use class.variable to access static variable
#         print('Employee Name:',self.n)
#         print('Employee ID:',self.i)
#         print('Salary:',self.s)
#         print('Designation:',self.d)
# obj=Employee()
# obj.setval('Gopika',2489,50000,'Data Scientist')
# obj.display()
#
# obj2=Employee()
# obj2.setval('Alex',2345,45000,'Data Engineer')
# obj2.display()


# Q: Create a class student with attributes student_name,roll_no,department,total_score with static variables
# college_name,college_email,location.Create 3 student objects
# A:
class Student:
    college_name='Nehru Arts and Science College'
    college_email='nasc@gmail.com'
    location='Padnekkad'
    def setval(self,name,roll_no,department,total_score):
        self.n=name
        self.r=roll_no
        self.d=department
        self.ts=total_score
    def display(self):
        print('College:',Student.college_name)
        print('College Email:',Student.college_email)
        print('Location:',Student.location)
        print('Student Name:',self.n)
        print('Roll No:',self.r)
        print('Department:',self.d)
        print('Total Score:',self.ts)
a=Student()
a.setval('Gopika Pavithran',26,'Statistics',700)
a.display()

b=Student()
b.setval('Hari',27,'Statistics',650)
b.display()

c=Student()
c.setval('Athul',34,'Economics',840)
c.display()