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