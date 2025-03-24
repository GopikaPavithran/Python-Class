# # Download XAMPP  - setting up a local server environment
#                   # in XAMPP server Start Apache and MySQL. view MySQL Admin to see databases
# # Install pymysql package (pip install pymysql)
#
import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='')
# mycursor=mydb.cursor()
# sql='create database Luminar'
# mycursor.execute(sql)
# print('Database Created Successfully')


# Q: Create a database using user input
db=pymysql.connect(host='localhost',user='root',password='')
cursor=db.cursor()
dbname=input('Enter your database name:')
sqlquery='create database %s'%dbname
cursor.execute(sqlquery)
print('Database Created successfully')