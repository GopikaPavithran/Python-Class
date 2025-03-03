# # Q: Check a number is odd or even
# # A:
# x=lambda n:'Even'if(n%2==0)else'Odd'
# print(x(6))
# print(x(3))


# # Q: Find largest of 2 numbers
# # A:
# largest=lambda a,b:a if a>b else b
# print(largest(4,8))
# print(largest(98,43))


# # Q: Find largest of 3 numbers
# # A:
# largest=lambda a,b,c: a if a>b and a>c else(b if b>c else c)
# print(largest(4,8,9))


# # Q: Find the largest of 4 numbers using lambda (user input)
# # A:
# a=int(input('Enter a:'))
# b=int(input('Enter b:'))
# c=int(input('Enter c:'))
# d=int(input('Enter d:'))
# largest=lambda a,b,c,d:a if (a>b and a>c and a>d) else(b if (b>c and b>d) else(c if (c>d) else d))
# print(largest(a,b,c,d))


# # Q: Absolute Conversion
# a=int(input('Enter a number:'))
# absolute=lambda a: a if a>0 else a*-1
# print(absolute(a))


# # Q: Convert numbers from positive to negative and negative to positive
# # A:
# a=int(input('Enter a number:'))
# x=lambda a:a*-1
# print(x(a))


# Q: Check a number is positive negative or zero
# A:
a=int(input('Enter a number:'))
x=lambda a:'Positive' if a>0 else('Zero' if a==0 else 'Negative')
print(x(a))