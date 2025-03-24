import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
# sql='select * from student_details order by name'    # ascending by default
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print(i)


# sql='select * from student_details order by name desc'    # descending
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print(i)


# Q: Select details of employee order by salary
# A:
sql='select * from employee_details order by salary'
mycursor.execute(sql)
a=mycursor.fetchall()
for i in a:
    print(i)