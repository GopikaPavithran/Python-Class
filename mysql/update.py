import pymysql
# mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
# mycursor=mydb.cursor()
# id=int(input('Enter ID:'))
# phone=int(input('Enter new phone number:'))
# sql='update student_details set phone=%d where id=%d'%(phone,id)
# mycursor.execute(sql)
# mydb.commit()


# # Q: Write an SQL query to update fee of student using name and email id.
# # A:
# n=input('Enter Name:')
# e=input('Enter Email ID:')
# f=int(input('Enter Fees:'))
# sql='update student_details set fee=%d where name="%s" and email="%s"'%(f,n,e)
# mycursor.execute(sql)
# mydb.commit()


# Update using condition
#-----------------------

mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
id=int(input('Enter ID:'))
name=input('Enter name:')
sql='select id from student_details'
mycursor.execute(sql)
a=mycursor.fetchall()
# print(a)    # output - ((1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,), (10,), (11,))
for i in a:
    if(id==i[0]):
        sql1='update student_details set name="%s" where id=%d'%(name,id)
        mycursor.execute(sql1)
        mydb.commit()
        print('Updated')
        break
else:
    print('ID Not Found')