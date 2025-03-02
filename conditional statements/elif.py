# syntax
# if (condition1):
#     body of if
# elif (condition2):
#     body of elif
# elif (condition3):
#     body of elif
# ..................
# ..................
# else:
#     body of else


# # Q: Check a number is +ve , -ve or Zero
# # A:
# n=int(input("Enter a number:"))
# if(n>0):
#     print("Positive")
# elif(n==0):
#     print("Zero")
# else:
#     print("Negative")


# # Q: Accept the percentage from the user and display the grade according to the following criteria
# # 81 - 100 : A+
# # 71 - 80 : A
# # 61 - 70 : B+
# # 51 - 60 : B
# # 41 - 50 : C+
# # 31 - 40 : C
# # 30 and below : Failed
#
# # A:
# n=int(input("Enter your percentage:"))
# if(81<=n<=100):
#     print('A+')
# elif(71<=n<=80):
#     print('A')
# elif(61<=n<=70):
#     print('B+')
# elif(51<=n<=60):
#     print('B')
# elif(41<=n<=50):
#     print('C+')
# elif(31<=n<=40):
#     print('C')
# else:
#     print("Failed")


# # Q: Find Largest of 3 numbers
# # A:
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter third number:"))
# if(a>b and a>c):
#     print(a,'is largest')
# elif(b>c):
#     print(b,'is largest')
# else:
#     print(c,'is largest')


# # Q: Accept the age of 4 people and display the youngest one
# # A:
# a=input("Name:")
# a1=int(input("Age:"))
# b=input("Name:")
# b1=int(input("Age:"))
# c=input("Name:")
# c1=int(input("Age:"))
# d=input("Name:")
# d1=int(input("Age:"))
# if(a1<b1 and a1<c1 and a1<d1):
#     print(a,'is the Youngest')
# elif(b1<c1 and b1<d1):
#     print(b,'is the Youngest')
# elif(c1<d1):
#     print(c,'is the Youngest')
# else:
#     print(d,'is the Youngest')


# # Q: Accept the cost price of a bike and display the road tax to be paid according to the following criteria
# # Cost Price                    Tax
# # >100000                       15%
# # 50000 and <= 100000           10%
# # <=50000                       5%
# # A:
# p=int(input("Enter the price of your bike:"))
# if(p>100000):
#     print("Tax=",15/100*p)
# elif(100000>=p>50000):
#     print("Tax=",10/100*p)
# else:
#     print("Tax=",5/100*p)


# # Q: A company decided to give bonus to employee according to the following criteria
# # Time period of service          Bonus
# # More than 10 years              10%
# # >=6 and <=10                    8%
# # less than 6 years               5%
# # A:
# t=int(input("Enter the time period of service:"))
# s=int(input("Enter your salary:"))
# if(t>10):
#     print('Bonus=',10/100*s)
# elif(6<=t<=10):
#     print('Bonus=',8/100*s)
# else:
#     print('Bonus=',5/100*s)


# # Q: Accept 2 numbers and mathematical operators and perform operations
# # A:
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# o=input('Enter an operator:')
# if(o=='+'):
#     print(a+b)
# elif(o=='-'):
#     print(a-b)
# elif(o=='*'):
#     print(a*b)
# elif(o=='/'):
#     print(a/b)
# else:
#     print('Invalid Operator')


# Q: Accept age,sex(M/F),number of days of work and display the wages accordingly
# Age                 Sex    Wage/day
# >=18 and <30        M      700
#                     F      750
# >=30 and <=40       M      800
#                     F      850
# A:
a=int(input('Age:'))
s=input('Gender:')
d=int(input('Number of days of work:'))
if(18<=a<30 and s=='M'):
    print('Wage=',d*700)
elif(18<=a<30 and s=='F'):
    print('Wage=',d*750)
elif(30<=a<=40 and s=='M'):
    print('Wage=',d*800)
elif(30<=a<=40 and s=='F'):
    print('Wage=',d*850)
else:
    print('Invalid')
