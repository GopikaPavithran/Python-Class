import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='select min(salary) from employee_details'
# mycursor.execute(sql)
# a=mycursor.fetchone()
# # print(a)   # output - (20000,)
# print('Minimum Salary=',a[0])


# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='select max(salary) from employee_details'
# mycursor.execute(sql)
# a=mycursor.fetchone()
# print('Maximum Salary:',a[0])


mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
sql='select min(salary),max(salary),avg(salary),sum(salary) from employee_details'
mycursor.execute(sql)
a=mycursor.fetchone()
print('Minimum Salary:',a[0],'\nMaximum Salary:',a[1],'\nAverage Salary:',a[2],'\nSum of Salary:',a[3])