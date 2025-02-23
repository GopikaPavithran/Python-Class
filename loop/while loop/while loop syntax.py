# Syntax
# while(condition):
#     body of while loop


# # Q: Print first 10 natural numbers using while loop
# # A:
# i=1
# while(i<11):
#     print(i)
#     i+=1


# # Q: Print from 1000 to 2000
# # A:
# i=1000
# while(i<=2000):
#     print(i)
#     i+=1


# # Q: Print first 10 even numbers
# # A:
# i=2
# while(i<=20):
#     if i%2==0:
#         print(i)
#     i+=1

            # OR

# i=2
# while(i<=20):
#     print(i)
#     i+=2


# # Q: 5,10,...30
# # A:
# i=5
# while(i<=30):
#     print(i,end=',')
#     i+=5
# print('\b')


# # Q: Reverse of natural numbers from 10 to 1
# # A:
# i=10
# while(i>=1):
#     print(i,end=',')
#     i-=1
# print('\b')


# Q: Odd numbers between the range input by the user
# A:
i=int(input('Enter initial range:'))
f=int(input('Enter final range:'))
while(i<=f):
    if(i%2!=0):
        print(i)
    i+=1
