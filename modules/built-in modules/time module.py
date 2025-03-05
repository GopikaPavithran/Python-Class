import time

# # Local time
# l=time.localtime()   # output as a tuple
# # print(l)
# print('Year:',l.tm_year)   # to access year
# print('Week day:',l.tm_wday)  #to access week day as index


# # asctime() - Human readable format
# print(time.asctime())


# # To delay the execution
# time.sleep(2.5)
# print('This prints after 2.5 seconds')


# To custom format date and time
# Q: Custom format - Friday 2023 Nov 3
# A:
print(time.strftime("%A %Y %b %d"))


# Note
# ----

# %Y - Year	(2025)
# %y - Year (25)
# %m - Month number (03)
# %B - Full month name	(March)
# %b - Abbreviated month name (Mar)
# %d - Day of the month 01 t0 31 (05)
# %H - Hour (24-hour format)
# %I - Hour (12-hour format)
# %M - Minute (00-59)
# %S - Second (00-59)
# %p - AM/PM
# %A - Full weekday name (Tuesday)
# %a - Abbreviated weekday (Tue)
# %w - Weekday number (0=Sunday)
# %j - Day of the year (001-366)
# %U - Number of week (Sunday as first day)
# %W - Number of week (Monday as first day)
