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
# def quadratic_solution(a,b,c):
#     d = b ** 2 - 4 * a * c
#     if d>0:
#         print((-b + d**0.5) / (2*a))
#         print((-b - d**0.5)/ (2*a))
#     elif d==0:
#         print(-b/(2*a))
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


# # Types of Arguments
# # ------------------
#
# # 1.Positional Argument
#
# def sum(a,b,c):
#     print(a+b+c)
# sum(6,9,33)



# # 2.Arbitrary Argument
#
# # Q: Find the sum of all numbers passing into a function using arbitrary arguments
# # A:
# def sum(*n):
#     s=0
#     for i in n:
#         s+=i
#     print('sum =',s)
# sum(3,5,7)


# # Q: Find product of numbers passing into a function
# # A:
# def product(*n):
#     p=1
#     for i in n:
#         p*=i
#     print(p)
# product(0,4,6)
# product(4,6,2,1)


# # Q: Find the largest number from the numbers passing into a function
# # A:
# def largest(*n):
#     l=n[0]
#     for i in n:
#         if i>l:
#             l=i
#     print(l)
# largest(4,77,43,876,234)
# largest(-3,-1,-44)


# # # Q: Find the smallest number from the numbers passing into a function
# # # A:
# def smallest(*n):
#     s=n[0]
#     for i in n:
#         if i<s:
#             s=i
#     print(s)
# smallest(356,23,78,3,78)
# smallest(-55,-2,-78,-3)


# # 3.Default Argument
#
# def add(a,b,c=0):
#     print(a+b+c)
# add(3,5,6)
# add(3,5)     # c=0 by default


# # Q: Using default argument create a function to find the largest from 4 numbers
# # A:
# def largest(a,b,c=0,d=0):
#     if a>b and a>c and a>d:
#         print(a)
#     elif b>c and b>d:
#         print(b)
#     elif c>d:
#         print(c)
#     else:
#         print(d)
# largest(56,22,68,44)
# largest(33,87,4)
# largest(56,9323)


# # 4.Keyword Argument
#
# def sum(a,b,c):
#     print(a+b+c)
# sum(c=4,a=5,b=3)


# # 5.Arbitrary Keyword Argument
#
# def name(**keyargs):
#     print(keyargs)
# name(firstname='a',middlename='b',lastname='c')


# # Q: Pass key value pairs into function and iterate both keys and values separately
# # A:
# def person(**keyarg):
#     for i,j in keyarg.items():
#         print(i,j)
# person(Name='Gopika',Age=22,Stream='Statistics',College='NASC')


# # Q: Sort {b:2,c:3,a:1}
# # A:
# def sort(**keyarg):
#     li=list(keyarg)
#     li.sort()
#     new={}
#     for i in li:
#         new.update({i:keyarg.get(i)})
#     print(new)
# sort(b=2,c=3,a=1)



