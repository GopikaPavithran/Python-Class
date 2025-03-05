import calendar


# # To print month
# y=int(input('Enter year:'))
# m=int(input('Enter month:'))
# print(calendar.month(y,m))


# # To print year
# y=int(input('Enter year:'))
# print(calendar.calendar(y))


# # To adjust the spacing
# print(calendar.calendar(2030,3,1,5,4))   # year,width,length, space between months, no.of months in a row


# # In python week starts from monday( index 0)
#
# #To customize starting day of week
# c=calendar.TextCalendar(calendar.SUNDAY)
# print(c.formatyear(2030))
# print(c.formatmonth(2025,3))


# # To check leap year
# print(calendar.isleap(2024))


help(calendar)