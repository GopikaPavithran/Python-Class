import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='insert into employee_details(name,salary)values("Alex",57000)'
# mycursor.execute(sql)
# mydb.commit()
# print('Data Added Successfully')


# # Q: Insert data using user input
# # A:
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# name=input('Enter your name:')
# salary=int(input('Enter salary:'))
# sql='insert into employee_details(name,salary)values("%s",%d)'%(name,salary)
# mycursor.execute(sql)
# mydb.commit()
# print('Data added successfully')


# # Q: Take number of employees from the user and insert the data
# # A:
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# n=int(input('Enter no.of employees:'))
# for i in range(n):
#     name=input('Enter employee name:')
#     salary=int(input('Enter salary:'))
#     sql='insert into employee_details(name,salary)values("%s",%d)'%(name,salary)
#     mycursor.execute(sql)
# mydb.commit()
# print(n,'Rows added')


# Q: Insert 5 data into student_details table.
# A:
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
for i in range(5):
    name=input('Enter student name:')
    email=input('Enter email:')
    qual=input('Enter qualification:')
    fee=int(input('Enter fee:'))
    phone=int(input('Enter phone number:'))
    sql='insert into student_details(name,email,qualification,fee,phone)values("%s","%s","%s",%d,%d)'%(name,email,qual,fee,phone)
    mycursor.execute(sql)
mydb.commit()
print('5 rows added')