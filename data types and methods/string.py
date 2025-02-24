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



# String Checking Methods
# -----------------------

# 1.isalpha()
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



# String Iteration
# ----------------

a=input("Enter a string:")
for i in a:
    print(i)