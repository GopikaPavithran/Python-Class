# # Syntax
# try:
#     code to be executed
# except:
#     run when an error occur


# # ZeroDivisionError
# # -----------------
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# print('Answer=',a/b)
# #
# # here if b=0 a ZeroDivisionError will occur. and it shows to the user as error.
# # This error will cause the program to terminate, and a traceback (including the error message and
# # line numbers) will be displayed to the user. This is generally not user-friendly.
# # we can use try...except to handle the error: The try block encloses the code that might cause the error and
# # instead of displaying a technical traceback, the except block prints a clear and informative message for user.
#
# try:
#     a=int(input('Enter first number:'))
#     b=int(input('Enter second number:'))
#     print('Answer=',a/b)
# except:
#     print('Error : Cant divide by zero')


# # ValueError
# # ----------
# try:
#     num=int(input('Enter a number:'))
#     print(num)
# except:
#     print('Invalid input. Please enter an integer')


# # Index Error
# # -----------
# try:
#     li=[3,7,'d',0,'b',4,8,'a','c']
#     n=int(input('Enter an index:'))
#     print(li[n])
# except:
#     print('Index out of range')


# FileNotFoundError
# -----------------
import os
try:
    f=input('Enter file name:')
    os.remove(rf'C:\Users\gopik\PycharmProjects\Python-Class\{f}')
    print('File Removed')
except:
    print('File Not Found')
