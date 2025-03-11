class Employee:
    company_name='TCS'       # static variable
    def setval(self,name,id,salary,designation):
        self.n=name
        self.i=id
        self.s=salary
        self.d=designation
    def display(self):
        print('Company Name:',Employee.company_name)   # use class.variable to access static variable
        print('Employee Name:',self.n)
        print('Employee ID:',self.i)
        print('Salary:',self.s)
        print('Designation:',self.d)
obj=Employee()
obj.setval('Gopika',2489,50000,'Data Scientist')
obj.display()

obj2=Employee()
obj2.setval('Alex',2345,45000,'Data Engineer')
obj2.display()

