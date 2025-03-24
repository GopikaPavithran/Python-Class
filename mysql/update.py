import pymysql
mydb=pymysql.connect(host='localhost',user='root',password='',database='luminar')
mycursor=mydb.cursor()
# id=int(input('Enter ID:'))
# phone=int(input('Enter new phone number:'))
# sql='update student_details set phone=%d where id=%d'%(phone,id)
# mycursor.execute(sql)
# mydb.commit()
# print('Phone Number Updated..')


# Q: Write an SQL query to update fee of student using name and email id.
# A:
n=input('Enter Name:')
e=input('Enter Email ID:')
f=int(input('Enter Fees:'))
sql='update student_details set fee=%d where name="%s" and email="%s"'%(f,n,e)
mycursor.execute(sql)
mydb.commit()
print('Fee Updated..')