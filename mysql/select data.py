import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='select * from employee_details'  # * is a universal symbol that is used to select all data
# mycursor.execute(sql)
# a=mycursor.fetchall()  # fetchall - a function used to fetch multiple data from a database. it returns tuple of tuples
# # print(a)
# for i in a:
#     # print(i)
#     print('ID:',i[0],'Name:',i[1],'Salary:',i[2])


# Q: Select data from student_details table.
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
sql='select * from student_details'
mycursor.execute(sql)
a=mycursor.fetchall()
for i in a:
    print('Details of',i[1],'\nID:',i[0],'\nEmail:',i[2],'\nQualification',i[3],'\nFees:',i[4],'\nPhone:',i[5])
