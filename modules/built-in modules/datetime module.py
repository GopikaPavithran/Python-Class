import datetime


# year=int(input('Enter year:'))
# month=int(input('Enter month:'))
# date=int(input('Enter date:'))
# mydate=datetime.date(year,month,date)
# print(mydate)
# print(type(mydate))


# # To fetch today's date
# t=datetime.date.today()
# print(t)


# # To take current year/month
# t=datetime.date.today()
# print(t.year)
# print(t.month)


# # To display current date and time
from datetime import datetime
# now=datetime.now()
# print(now)


# # To find particular date before or after from today
from datetime import timedelta
from datetime import date
d=date.today()
# d+=timedelta(days=15)
# print(d)

# d+=timedelta(days=100)    # 100 days after today
# print(d)

d-=timedelta(days=100)    # 100 days before today
print(d)