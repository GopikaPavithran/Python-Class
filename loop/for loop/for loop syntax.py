# # Syntax
# for i in range(n):
#      body of for loop


# # Q: Take range from user and print 'Hai'
# # A:
# n=int(input('Enter range:'))
# for i in range(n):
#      print('Hai')


# # Q: Print first 10 natural numbers
# # A:
# for i in range(10):
#     print(i+1)
#
           #OR
#
# for i in range(1,11):
#     print((i))


# # Q: Print numbers between the range input by the user
# # A:
# n=int(input('Enter initial range:'))
# m=int(input('Enter final range:'))
# for i in range(n,m+1):
#     print(i)


# # Q: Print first 5 even numbers
# # A:
# for i in range(1,11):
#     if i%2==0:
#         print(i)


# # Q: Print odd numbers between the range 100,200
# # A:
# for i in range(100,200):
#     if i%2!=0:
#         print(i)


# # Q:Take initial value final value from the user and print even numbers between the range
# # A:
# n=int(input('Enter initial range:'))
# m=int(input('Enter final range:'))
# for i in range(n,m+1):
#     if i%2==0:
#         print(i)


# Q: Print multiplication table of a number input by the user
# A:
n=int(input('Enter a number:'))
for i in range(1,11):
    print(n,'x',i,'=',n*i)

