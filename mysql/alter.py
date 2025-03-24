# # To add single column
# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='alter table student_details add totalmark float(4)'    # alter - to do changes
# mycursor.execute(sql)
# mydb.commit()
# # a column with null values will be created


# # To add multiple columns
# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='alter table student_details add(age int (2) , gender varchar(10))'
# mycursor.execute(sql)
# mydb.commit()


# # To add column in a specific position
# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='alter table student_details add last_name varchar(15) after name'
# mycursor.execute(sql)
# mydb.commit()


# # To delete single column
# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='alter table student_details drop column last_name'
# mycursor.execute(sql)
# mydb.commit()


# # To delete multiple columns
# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='alter table student_details drop column gender, drop column totalmark'
# mycursor.execute(sql)
# mydb.commit()


# To add a column with values
import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='employee')
mycursor=mydb.cursor()
sql='alter table employee_qualification add Total_Mark int as(Maths+Chemistry+Physics)'
mycursor.execute(sql)
mydb.commit()


