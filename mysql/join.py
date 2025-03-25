# # Creating new database with 2 tables(3 rows for each)
import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='')
# mycursor=mydb.cursor()
# sql1='create database Employee'
# mycursor.execute(sql1)
# mydb.select_db('Employee')
# sql2='create table Employee_Details(Id int auto_increment, First_Name varchar(15), Last_Name varchar(15), Email varchar(40), Job_Title Varchar(30), Department_ID int(2), Salary int(6), primary key(id))'
# mycursor.execute(sql2)
# sql3='create table Employee_Qualification(Id int auto_increment, First_Name varchar(15), Last_Name varchar(15), Qualification varchar(20), Maths int(3), Chemistry int(3), Physics int(3), primary key(id))'
# mycursor.execute(sql3)
# for i in range(3):
#     fn=input('First name:')
#     ln=input('Last name:')
#     e=input('Email:')
#     j=input('Job title:')
#     d=int(input('Department id:'))
#     s=int(input('Salary:'))
#     q=input('Qualification:')
#     m=int(input('Maths:'))
#     c=int(input('Chemistry:'))
#     p=int(input('Physics:'))
#     sql4='insert into Employee_details (First_Name, Last_Name, Email , Job_Title , Department_ID, Salary) values("%s","%s","%s","%s",%d,%d)'%(fn,ln,e,j,d,s)
#     mycursor.execute(sql4)
#     sql5='insert into Employee_Qualification(First_Name, Last_Name, Qualification, Maths, Chemistry, Physics) values("%s","%s","%s",%d,%d,%d)'%(fn,ln,q,m,c,p)
#     mycursor.execute(sql5)
# mydb.commit()


mydb=pymysql.connect(host='localhost',user='root',password='',database='employee')
mycursor=mydb.cursor()
# sql='select employee_details.First_Name,employee_details.Last_Name,employee_qualification.Qualification from employee_details inner join employee_qualification on employee_details.First_Name=employee_qualification.First_Name'
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print(i)


# # task:

# # 1. Display first name, last name, department id total mark of employee
# # A:
# sql='select employee_details.First_Name,employee_details.Last_Name,employee_details.Department_ID,employee_qualification.Total_Mark from employee_details inner join employee_qualification on employee_details.First_Name=employee_qualification.First_Name'
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print(i)

# # 2. Create a new column PF in employee details. PF:15% of salary
# # A:
# sql='alter table employee_details add PF int as(salary/100*15)'
# mycursor.execute(sql)
# mydb.commit()


# # 3. Print the total salary
# # A:
# sql='select sum(salary) from employee_details'
# mycursor.execute(sql)
# a=mycursor.fetchone()
# print(a[0])


# # 4. Print the minimum,maximum,average of the salary
# # A:
# sql='select min(salary),max(salary),avg(salary) from employee_details'
# mycursor.execute(sql)
# a=mycursor.fetchall()
# # print(a)     # output - ((50000, 100000, Decimal('75000.0000')),)      - Decimal('75000.0000') because MySQL AVG() function can return
# #                                                                           decimal values, and pymysql preserves this precision by returning
# #                                                                           the result as a Decimal object.
# # print(a[0])  # output - (50000, 100000, Decimal('75000.0000'))
# print('Minimum:',a[0][0],'\nMaximum:',a[0][1],'\nAverage:',int(float(a[0][2])))
#                                                         # int(float(a[0][2])):
#                                                         # a[0][2] is the Decimal object representing the average salary.
#                                                         # float(a[0][2]) converts it to a regular Python float.
#                                                         # int(...) then converts the float to an integer, truncating any decimal part.


# 5. Print employee details in descending order of name
# A:
sql='select * from employee_details order by First_Name desc'
mycursor.execute(sql)
a=mycursor.fetchall()
for i in a:
    print(i)