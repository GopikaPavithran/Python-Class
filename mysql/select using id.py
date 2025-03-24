import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
n=int(input('Enter ID:'))
sql='select * from employee_details where id=%d'%n     # where - to filter records from a database table based on specified conditions
mycursor.execute(sql)
a=mycursor.fetchone()     # fetchone - used to fetch a single row of data. it returns a single tuple.
print('ID:',a[0],'\nName:',a[1],'\nSalary:',a[2])
