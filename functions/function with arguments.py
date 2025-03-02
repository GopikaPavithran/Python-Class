# def add(a,b):
#     print(a+b)
# add(3,5)


# # Q: Define a function to find the product of 3 numbers using function with arguments
# # A:
# def product(a,b,c):
#     print(a*b*c)
# product(4,1,2)


# # Q: Define a function to find area of a triangle
# # A:
# def triangle_area(b,h):
#     print('area =',(1/2)*b*h)
# triangle_area(4,6)


# # Q: Define a function to find factorial
# # A:
# def factorial(n):
#     f=1
#     for i in range(1,n+1):
#         f*=i
#     print(f)
# factorial(5)


# # Q: Define a function to generate multiplication table
# # A:
# def multiplication(n):
#     for i in range(1,11):
#         print(n,'x',i,'=',i*n)
# multiplication(5)


# # Q: Define a function to print reverse of a number
# # A:
# def reverse(n):
#     s=str(n)
#     rev=s[::-1]
#     print(rev)
# reverse(100)
# reverse(123)


# # Q: Define a function to check a string is palindrome or not
# # A:
# def palindrome(s):
#     if s[::-1]==s:
#         print('palindrome')
#     else:
#         print('Not Palindrome')
# palindrome('python')
# palindrome('malayalam')


# # Q: Define a function to find product of digits of number
# # A:
# def product_digit(n):
#     p=1
#     l=len(str(n))
#     for i in range(l):
#         r=n%10
#         p*=r
#         n//=10
#     print(p)
# product_digit(65)
# product_digit(360)


# # Q: Define a function to find sum of factors of a number
# # A:
# def factor_sum(n):
#     s=0
#     for i in range(1,n+1):
#         if n%i==0:
#             s+=i
#     print(s)
# factor_sum(12)


# # Q: Define a function to solve quadratic equation (-b +or- root of b^2 - 4ac / 2a)
# # A:
# import math
# def quadratic_solution(a,b,c):
#     d = b ** 2 - 4 * a * c
#     if d>0:
#         print(((-1*b) + math.sqrt(d)) / 2*a)
#         print(((-1*b) - math.sqrt(d)) / 2*a)
#     else:
#         print('Not a real number')
# quadratic_solution(1,5,4)
# quadratic_solution(3,2,4)


# # Q: Define a function to check a number is prime or not
# # A:
# def prime(n):
#     factor_count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             factor_count+=1
#     if factor_count==2:
#         print('Prime')
#     else:
#         print('Not prime')
# prime(4)
# prime(11)
# prime(1)
# prime(2)

                     # OR

# def prime(n):
#     if n<=1:
#         print('Not Prime')
#     else:
#         for i in range(2,n):
#             if n%i==0:
#                 print('Not prime')
#                 break
#         else:
#             print('Prime')
# prime(7)
# prime(9)
# prime(1)