# # Q: Find the product of first 10 natural numbers
# # A:
# p=1
# for i in range(1,11):
#     p*=i
# print('Product =',p)


# # Q: Print 1 to 100 except the multiple of 2 and 3
# # A:
# for i in range(1,101):
#     if i%2!=0 and 1%3!=0:
#         print(i,end=',')
# print('\b')


# # Q: Find factorial of a number input by the user
# # A:
# n=int(input('Enter a number:'))
# f=1
# for i in range(1,n+1):
#     f*=i
# print(n,'! =',f)


# # Q: Find sum of digits of a number input by the user
# # A:
# n=int(input('Enter a number:'))
# s=0
# l=len(str(n))
# for i in range(l):
#     r=n%10
#     s+=r
#     n//=10
# print('Sum of digits =',s)


# # Q: Find Product of digits of a number input by the user
# # A:
# n=int(input('Enter a number:'))
# p=1
# l=len(str(n))
# for i in range(l):
#     r=n%10
#     p*=r
#     n//=10
# print('Product of digits =',p)


# Q: Print fibonacci series
# A:
n=int(input("Enter a limit:"))
a=0
b=1
print(a)
print(b)
for i in range(n-2):
    c=a+b
    print(c)
    a=b
    b=c



