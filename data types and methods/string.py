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


# # Q: Check a string input by the user is palindrome or not (using index)
# # A:
# s=input('Enter a string:')
# if s[::-1]==s:
#     print('Palindrome')
# else:
#     print('Not Palindrome')


# # Q: Find length of the string input by the user without using len()
# # A:
# a=input('Enter a string:')
# c=0
# for i in a:
#     c+=1
# print('Length of the string =',c)


# # Q: Find length without including white space
# # A:
# a=input('Enter a string:')
# c=0
# for i in a:
#     if i!=' ':
#         c+=1
# print('Length of the string =',c)


# # Q: Count the total numer of digits and alphabets in an alphanumeric string input by the user
# # A:
# a=input('Enter a string:')
# ac=0
# dc=0
# for i in a:
#     if i.isalpha():
#         ac+=1
#     elif i.isnumeric():
#         dc+=1
# print('Count of alphabets=',ac)
# print('Count of digits=',dc)


# # Q: Count total number of vowels in a string input by the user
# # A:
# a=input('Enter a string:').lower()
# vc=0
# for i in a:
#     if i in 'aeiou':
#         vc+=1
# print('Count of vowels=',vc)


# # Q: Print the total count of upper case and lower case letters in a string input by the user
# # A:
# a=input('Enter a string:')
# uc=0
# lc=0
# for i in a:
#     if i.isupper():
#         uc+=1
#     elif i.islower():
#         lc+=1
# print('Count of upper case letters=',uc)
# print('Count of lower case letters=',lc)


# # Q: Remove duplicate elements from a string input ny the user
# # A:
# temp=''
# a=input('Enter a string:')
# for i in a:
#     if i not in temp:
#         temp+=i
# print(temp)


# # Q: Take 3 strings from the user and display the largest string
# # A:
#           # without sing len()
#
# a=input('Enter first string:')
# b=input('Enter second string:')
# c=input('Enter third string:')
# ac=0
# bc=0
# cc=0
# for i in a:
#     ac+=1
# for i in b:
#     bc+=1
# for i in c:
#     cc+=1
# if ac>bc and ac>cc:
#     print('The largest string is ','"',a,'"')
# elif bc>cc:
#     print('The largest string is ', '"',b, '"')
# else:
#     print('The largest string is ', '"',c, '"')

#              # using len()
#
# a=input('Enter first string:')
# b=input('Enter second string:')
# c=input('Enter third string:')
# if len(a)>len(b) and len(a)>len(c):
#     print('The largest string is ', '"', a, '"')
# elif len(b)>len(c):
#     print('The largest string is ', '"', b, '"')
# else:
#     print('The largest string is ', '"', c, '"')


# # Q: Find a string is palindrome or not (using element accessing)
# # A:
# a=input("Enter a string:")
# rev=''
# last=len(a)-1
# for i in range(last,-1,-1):
#     rev+=a[i]
# if rev==a:
#     print('Palindrome')
# else:
#     print('Not Palindrome')


