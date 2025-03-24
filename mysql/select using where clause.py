import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# n=int(input('Enter ID:'))
# sql='select * from employee_details where id=%d'%n     # where - where is a clause used to filter records from a database table based on specified conditions
# mycursor.execute(sql)
# a=mycursor.fetchone()     # fetchone - used to fetch a single row of data. it returns a single tuple.
# print('ID:',a[0],'\nName:',a[1],'\nSalary:',a[2])


# # Q: Write a query to select details of students using qualification.
# # A:
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# qual=input('Enter qualification:')
# sql='select * from student_details where qualification="%s"'%qual
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print('ID:',i[0],', Name:',i[1],', Email:',i[2],', Qualification:',i[3],', Fees:',i[4],', Phone:',i[5])


# Using Logical Operators
# -----------------------

# and
# ---
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# name=input('Enter name:')
# email=input('Enter email:')
# sql='select * from student_details where name="%s" and email="%s"'%(name,email)
# mycursor.execute(sql)
# a=mycursor.fetchone()
# print(a)

# # or
# # --
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# name=input('Enter name:')
# email=input('Enter email:')
# sql='select * from student_details where name="%s" or email="%s"'%(name,email)
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print(i)

# not
# ---
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
name=input('Enter name:')
sql='select * from student_details where not name="%s"'%(name)
mycursor.execute(sql)
a=mycursor.fetchall()
for i in a:
    print(i)
