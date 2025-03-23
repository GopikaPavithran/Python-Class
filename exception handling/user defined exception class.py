# # Q: Take a number input from the user. define exceptions for zero and negative numbers
# # A:
# class ZeroException(Exception):   # should inherit the built-in Exception class.
#     pass
# class NegativeException(Exception):
#     pass
# try:
#     n=int(input('Enter a number:'))
#     if n==0:
#         raise ZeroException
#     elif 0>n:
#         raise NegativeException
#     else:
#         print('Positive Number')
# except ZeroException:
#     print('Zero error occurred')
# except NegativeException:
#     print('Negative error occurred')
# except ValueError as e:
#     print(e)


# # Q: Take a string as input if string has alphabets only print 'success'. else raise number error,
# # alphanumeric error,special character error.
# # A:
# class NumberError(Exception):
#     pass
# class AlphanumericError(Exception):
#     pass
# class SpecialCharacterError(Exception):
#     pass
# try:
#     s=input('Enter a string:')
#     if s.isalpha():
#         print('Success')
#     elif s.isnumeric():
#         raise NumberError
#     elif s.isalnum():
#         raise AlphanumericError
#     else:
#         raise SpecialCharacterError
# except NumberError:
#     print('Please input alphabets not numbers')
# except AlphanumericError:
#     print('Please input alphabets only')
# except SpecialCharacterError:
#     print('Please input alphabets only not special characters')


# Q: Take age as input if age is in between 21 and 40 print 'Eligible'. raise TooYoungException and
# TooOldException
# A:
class TooYoungException(Exception):
    pass
class TooOldException(Exception):
    pass
try:
    age=int(input('Enter your age:'))
    if 21<=age<=40:
        print('Eligible')
    elif age<21:
        raise TooYoungException
    elif age>40:
        raise TooOldException
except TooYoungException:
    print('Sorry! Not Eligible')
except TooOldException:
    print('Sorry! Not Eligible')
except ValueError as e:
    print(e)
