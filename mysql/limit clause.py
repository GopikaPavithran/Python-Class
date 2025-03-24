import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
# sql='select * from student_details limit 2'   # fetch data from first 2 row
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print(i)


# Q: Select details of students using qualification by limit clause
# A:
limit=int(input('Enter limit:'))
qual=input('Enter qualification:')
sql='select * from student_details where qualification="%s" limit %d'%(qual,limit)
mycursor.execute(sql)
a=mycursor.fetchall()
for i in a:
    print(i)