import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
# sql='select name,qualification from student_details'
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print('Name:',i[0],',Qualification:',i[1])


# Q: Write a query to select the name, email and phone number of student using name
n=input('Enter name:')
sql='select name,email,phone from student_details where name="%s"'%n
mycursor.execute(sql)
a=mycursor.fetchone()
print('Name:',a[0],',Email:',a[1],',Phone:',a[2])