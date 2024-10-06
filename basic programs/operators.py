# # ARITHMETIC OPERATORS(+,-,*,/,%,//,**)
# a=11
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)


# # Q:
# 1. Write a program to find square of a number input by the user
# 2. Find cube of a number input by the user
# 3. Write a program to find area of a circle
# 4. Write a program to find area of a triangle
# 5. Write a program to find the last digit of a number input by the user

# # A:
# 1.
# n=int(input("Enter a number:"))
# print("The square of",n,"is",n**2)

# 2.
# n=int(input("Enter a number:"))
# print("The cube of",n,"is",n**3)

# 3.
# r=int(input('Enter radius:'))
# print("Area=",3.14*r**2)

# 4.
# h=int(input("Enter Height:"))
# b=int(input("Enter Breadth:"))
# print("Area=",1/2*b*h)

# 5.
# n=int(input("Enter a number:"))
# print('Last Digit is',n%10)


# # ASSIGNMENT OPERATORS(=,+=,-=,*=,/=,%=,//==,**=)
# a=10
# print(a)
#
# a=10
# a+=2
# print(a)
#
# a=10
# a-=2
# print(a)
#
# a=10
# a*=2
# print(a)
#
# a=10
# a/=2
# print(a)
#
# a=10
# a%=2
# print(a)
#
# a=10
# a//=2
# print(a)
#
# a=10
# a**=2
# print(a)


# # COMPARISON OPERATORS(==,<,>,<=,>=,!=)
# a=10
# b=23
# print(a==b)
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a!=b)


# #LOGICAL OPERATORS(and,or,not)
# a=12
# b=23
# c=33
#
# #and:
# print(a<b and b<c)
# print(a<b and b>c)
# print(a>b and b>c)
#
# # Or:
# print(a<b or b<c)
# print(a<b or b>c)
# print(a>b or b>c)
#
# # not:
# print(not(a<b and b<c))
# print(not(a<b and b>c))
# print(not(a>b and b>c))
#
# print(not(a<b or b<c))
# print(not(a<b or b>c))
# print(not(a>b or b>c))


# # MEMBERSHIP OPERATORS(in,not in)
# str='hello'
# print('h' in str)
# print('h' not in str)


# IDENTITY OPERATORS(is,is not)
#string - immutable
a='hello'
b='hello'
print(a is b)
print(a is not b)
print(id(a))
print(id(b))

#list - mutable
a=['a','b','c']
b=['a','b','c']
print(a is b)
print(a is not b)
print(id(a))
print(id(b))









