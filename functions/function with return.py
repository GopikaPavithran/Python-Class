# def add(a,b):
#     return a+b
# print(add(5,8))


# # Q: Define a function to find a number is odd or even using return type
# # A:
# def odd_even(n):
#     if n%2==0:
#         return '%d is even'%n
#     else:
#         return '%d is odd'%n
# print(odd_even(6))


# # Q: create a function voting eligibility by passing name and age
# # A:
# def vote(name,age):
#     if age>=18:
#         return '%s is %d years old. Eligible for voting'%(name,age)
#     else:
#         return '%s is %d years old. Not eligible for voting' % (name, age)
# print(vote('Gopika',22))
# print(vote('Gobin',15))


# # Q: Accept the cost price of a bike and display the road tax to be paid according to the following criteria
# # Cost Price                    Tax
# # >100000                       15%
# # 50000 and <= 100000           10%
# # <=50000                       5%
# # A:
# def tax(cost):
#     if cost>100000:
#         return 15/100 *cost
#     elif cost<=100000 and cost==50000:
#         return 10/100*cost
#     else:
#         return 5/100*cost
# print(tax(50000))


# # Q: A company decided to give bonus to employee according to the following criteria
# # Time period of service          Bonus
# # More than 10 years              10%
# # >=6 and <=10                    8%
# # less than 6 years               5%
# # A:
# def bonus(time,salary):
#     if time>10:
#         return 10/100*salary
#     if 6<=time<=10:
#         return 8/100*salary
#     else:
#         return 5/100*salary
# print(bonus(4,25000))


# # Q: Check a number is divisible by both 2 and 3
# # A:
# def div(n):
#     if n%2==0 and n%3==0:
#         return '%d is divisible by both 2 and 3'%n
#     else:
#         return '%d is not divisible by both 2 and 3'%n
# print(div(15))


# # Q: Solve quadratic equation using function with multiple return
# # A:
# def quadratic(a,b,c):
#     d= b**2 - 4*a*c
#     if d>0:
#         root1= (-b + d**0.5) / 2*a
#         root2=(-b - d**0.5)/2*a
#         return root1,root2
#     elif d==0:
#         return None
#     else:
#         return 'Not real number'
# print(quadratic(1,5,4))
# print(quadratic(1,4,4))
# print(quadratic(6,3,4))


