# # Q: Find factorial of a number using while loop
# # A:
# n=int(input("Enter a number:"))
# f=1
# i=1
# while(i<=n):
#     f*=i
#     i+=1
# print(n,'! =',f)


# # Q: Display the numbers from 1 to 10 with their factorial value
# # A:
# f=1
# i=1
# while(i<=10):
#     f*=i
#     print(i,'! =',f)
#     i+=1


# # Q: Print numbers between 1 to 100 except the numbers which are divisible by 5 and 10
# # A:
# i=1
# while(i<=100):
#     if i%5!=0:
#         print(i)
#     i+=1


# # Q: Sum of first 10 natural numbers
# # A:
# s=0
# i=1
# while(i<=10):
#     s+=i
#     i+=1
# print('Sum =',s)


# # Q: Count of odd numbers between the range input by the user
# # A:
# i=int(input('Enter initial range:'))
# f=int(input('Enter final range:'))
# c=0
# while(i<=f):
#     if i%2!=0:
#         c+=1
#     i+=1
# print('Count of odd numbers =',c)


# # Q: Find the product of numbers between the range 1 to 100 except the multiple of 7 and 13
# # A:
# i=1
# p=1
# while(i<=100):
#     if i%7!=0 or 1%13!=0:
#         p*=i
#     i+=1
# print('Product =',p)


# # Q: Print first 10 natural numbers and their square
# # A:
# i=1
# while(i<=10):
#     print(i,' ',i**2)
#     i+=1


# # Q: Multiplication table generation
# # A:
# n=int(input("Enter a number:"))
# i=1
# while(i<=10):
#     print(n,'x',i,'=',n*i)
#     i+=1


# # Q: write a program to enter a number till the user enter 0 and at the end it should display the count of
# #    positive and negative values entered
# # A:
# n=int(input('Enter a number:'))
# pc=0
# nc=0
# while(n!=0):
#     if n>0:
#         pc+=1
#     else:
#         nc+=1
#     n=int(input('Enter a number:'))
# print('Count of positive numbers =',pc)
# print('Count of negative numbers =',nc)


# Q: write a program to enter a number till the user enter 0 or negative value and at the end it should display
# #    the count of even and odd number
# # A:
# n=int(input('Enter a number:'))
# oc=0
# ec=0
# while(n>0):
#     if n%2==0:
#         ec+=1
#     else:
#         oc+=1
#     n=int(input('Enter a number:'))
# print('Count of even numbers =',ec)
# print('Count of odd numbers =',oc)


# # Q: Find the sum of digits of a number input by the user
# # A:
# n=int(input('Enter a number:'))
# s=0
# while(n!=0):
#     r=n%10
#     s+=r
#     n//=10
# print('sum =',s)


# # Q: Find the product of digits of a number input by the user
# # A:
# n=int(input('Enter a number:'))
# p=1
# if n==0:
#     print('Product =',0)
# else:
#     while(n!=0):
#         r=n%10
#         p*=r
#         n//=10
#     print('Product =',p)

                            # OR

# n=int(input('Enter a number:'))
# temp=n
# p=1
# while(n!=0):
#     r=n%10
#     p*=r
#     n//=10
# if temp==0:
#     print('Product =',0)
# else:
#     print('Product =',p)


# # Q: Find reverse of number input by the user
# # A:
# n=int(input('Enter a number:'))
# rev=0
# while(n!=0):
#     r=n%10
#     rev=rev*10+r
#     n//=10
# print(rev)
#             # ---> if input = 100 , output = 1


# # Q: Check the number is palindrome or not
# # A:
# n=int(input('Enter a number:'))
# temp=n
# rev=0
# while(n!=0):
#     r=n%10
#     rev=rev*10+r
#     n//=10
# if temp==rev:
#     print('Palindrome')
# else:
#     print('Not Palindrome')


# Q: Check the number is armstrong or not
# A:
n=int(input("Enter a number:"))
temp=n
l=len(str(n))
a=0
while(n!=0):
    r=n%10
    a+=r**l
    n//=10
if a==temp:
    print('Armstrong number')
else:
    print('Not an armstrong number')







