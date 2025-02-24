# # Methods
# # -------

# # 1.upper()
# s='hello world'
# print(s.upper())


# # 2.lower()
# s="HELLO World"
# print(s.lower())


# # 3.title()
# s='hello world'
# print(s.title())


# # 4.capitalize()
# s='hello world'
# print(s.capitalize())


# # 5.swapcase()
# s='HelLO WoRld'
# print(s.swapcase())


# # 6.split()
# s='hello world'
# print(s.split())
#
# s='hello_world'
# print(s.split())
#
# s='hello_world'
# print(s.split('_'))
#
# s='hello/world/welcome/to/python'
# print(s.split('/',2))


# # 7.replace()
# s='hello world'
# print(s.replace('hello','hi'))


# # 8.strip()
# # --> Two types
# #     1.lstrip()
# #     2.rstrip()
# s=input("Enter a string:")
# print(s.strip())


# # 9.index()
# s='hello'
# print(s.index('h'))    # index starts with 0
#
# print(s.index('l'))    # returns position of first 'l'

# print(s.index('z'))    # shows error


# # 10.find()
# s='hello'
# print(s.find('e'))
#
# print(s.find('z'))     # returns -1



# # String Checking Methods
# # -----------------------
# #
# # 1.isalpha()
# s=input('Enter a string:')
# print(s.isalpha())


# # 2.isnumeric()
# s=input('Enter a string:')
# print(s.isnumeric())


# # 3.isalnum()
# s=input('Enter a string:')
# print(s.isalnum())


# # 4.istitle()
# s=input('Enter a string:')
# print(s.istitle())


# # 5.islower()
# s=input('Enter a string:')
# print(s.islower())


# # 6.isupper()
# s=input('Enter a string:')
# print(s.isupper())


# # 7.isspace()
# s=input('Enter a string:')
# print(s.isspace())



# # String Iteration
# # ----------------
#
# a=input("Enter a string:")
# for i in a:
#     print(i)


# # Q: Write a program to remove space character from a string input by the user without using any function
# # A:
# a=input("Enter a string:")
# for i in a:
#     if i!=' ':
#         print(i,end='')



# # String Slicing
# # --------------
#
# s='welcome to python'
# print(s[11:17])
#
# print(s[:7])          # starting to 6th index
#
# print(s[11:])         # 11th index to ending
#
# print(s[:])           # full string
#
# print(s[::-1])        # reverse


# Q: Check a string input by the user is palindrome or not
# A:
s=input('Enter a string:')
if s[::-1]==s:
    print('Palindrome')
else:
    print('Not Palindrome')

