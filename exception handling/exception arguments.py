# try:
#     a=int(input('Enter first number:'))
#     b=int(input('Enter second number:'))
#     print('Answer=',a/b)
# except ZeroDivisionError:               # ZeroDivisionError and ValueError are the possible errors here
#     print('Division by zero is not allowed.')
# except ValueError:
#     print('Invalid input. Please enter an integer')
#
# # here we used customized exception messages in the except blocks. instead of that we can use exception arguments
# # it shows the built-in exception message
#
#
# try:
#     a=int(input('Enter first number:'))
#     b=int(input('Enter second number:'))
#     print('Answer=',a/b)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)


# # Q: Solve quadratic equation using exception handling.
# # A:
# try:
#     a=int(input('Enter a:'))
#     b=int(input('Enter b:'))
#     c=int(input('Enter c:'))
#     d= b**2 - 4*a*c
#     if d>0:
#         print((-b + d**0.5)/(2*a))
#         print((-b - d**0.5)/(2*a))
#     elif d==0:
#         print(-b/(2*a))
#     else:
#         print('Not a real number')
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)


# # Exception raise keyword: used to raise an exception. it throws an error immediately at the running of
# # program by using the raise keyword.
#
#
# # Q: Check voting eligibility
# # A:
# try:
#     name=input('Enter Name:')
#     age=int(input('Enter Age:'))
#     if age>=18:
#         print(name,'is eligible for voting')
#     else:
#         raise Exception   #customized exception. can either raise a built-in exception (like ZeroDivisionError, ValueError, etc.) with a custom message
# except Exception:
#     print('Not eligible')
#
#
# try:
#     name=input('Enter Name:')
#     age=int(input('Enter Age:'))
#     if age>=18:
#         print(name,'is eligible for voting')
#     else:
#         raise Exception
# except ValueError as e:  # ValueError is also possible in this code.
#     print(e)
# except Exception:
#     print('Not eligible')
#
# # In Python, exceptions are processed in the order they are defined, so the more specific exceptions
# # (like ValueError) should be caught before the more general ones (like Exception).
# # This is because once an Exception is caught by a matching except block, the rest of the except blocks
# # are skipped.


# # Q: Take a number as user input. if number is positive print 'Registered' else raise an exception
# # A:
# try:
#     n=int(input('Enter a number:'))
#     if n>0:
#         print('Registered')
#     elif n<0:
#         raise Exception
# except ValueError as e:
#     print(e)
# except Exception:
#     print('Negative Value')


# # Q: Name input from user. ensure the name entered contains only alphabetic characters and print
# # 'Valid name'. else raise an exception
# # A:
# try:
#     name=input('Enter a name:')
#     if name.isalpha():
#         print('Valid name')
#     else:
#         raise Exception
# except Exception:
#     print('Please enter a valid name.')


# # Finally Block - finally block will be executed  no matter if the try block raises an error or not.
# # Exception handling else block - else block lets you execute a code when there is no error
#
# # Q: Check voting eligibility.(use finally block and else)
# # A:
# try:
#     name=input('Enter name:')
#     age=int(input('Enter Age:'))
#     if age>=18:
#         print(name,'is eligible for voting')
#     else:
#         print(name,'is not eligible for voting')
#     if name.isalpha()==False:
#         raise Exception
# except ValueError as e:
#     print(e)
# except Exception:
#     print('Please enter a valid name.')
# finally:
#     print('Task Completed')

try:
    name=input('Enter name:')
    age=int(input('Enter Age:'))
    if age>=18:
        print(name,'is eligible for voting')
    else:
        print(name,'is not eligible for voting')
    if name.isalpha()==False:
        raise Exception
except ValueError as e:
    print(e)
except Exception:
    print('Please enter a valid name.')
else:
    print('No error.Program successfully completed.')
finally:
    print('Task Completed')