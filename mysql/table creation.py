import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')    # should add database name.
# mycursor=mydb.cursor()
# sql='CREATE TABLE employee_details(id int auto_increment,name varchar(30),salary int(6),primary key(id))'
# mycursor.execute(sql)
# mydb.commit()   # to save any changes made during the session
# print('Table Created Successfully')

# Q: Create table student_details with columns id,name,email,qualification,fee,phone number.
# A:
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
sql='CREATE TABLE student_details(id INT AUTO_INCREMENT,name VARCHAR(25),email VARCHAR(50),qualification VARCHAR(50),fee INT(6),phone BIGINT,primary key(id))'
mycursor.execute(sql)
mydb.commit()
print('Table Created Successfully')