# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# id=int(input('Enter the id to delete:'))
# sql='delete from student_details where id=%d'%id
# mycursor.execute(sql)
# mydb.commit()


# # Truncate - delete data inside a table not the structure (truncate table tablename)
# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='truncate table employee_details'
# mycursor.execute(sql)
# mydb.commit()


# # Drop - delete data with table structure
# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='drop table employee_details'
# mycursor.execute(sql)
# mydb.commit()


# # # To delete a database
# import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# sql='drop database gopika'
# mycursor.execute(sql)
# mydb.commit()
