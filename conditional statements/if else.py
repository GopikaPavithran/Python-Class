# # Syntax
# if (condition):
#     body of if
# else:
#     body of else
# eg:
# n=input("Enter an alphabet:")
# if(n in "aeiou"):
#     print('Vowel')
# else:
#     print('Not a Vowel')


# # Q: find largest of two numbers input by the user
# # A:
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# if(a>b):
#     print(a,"is largest")
# else:
#     print(b,'is largest')


# Q: find largest of two numbers input by the user
# # A:
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# if(a<b):
#     print(a,"is smallest")
# else:
#     print(b,'is smallest')


# # Q: Voting eligibility checking (name,age)
# # A:
# n=input('Name:')
# a=int(input('Age:'))
# if(a>=18):
#     print(n,'is eligible for voting')
# else:
#     print(n,'is not eligible for voting')


# # Q: Check a number is odd or even
# # A:
# n=int(input('Enter a number:'))
# if(n%2==0):
#     print("Even")
# else:
#     print("Odd")


# # Q: Check a number input by the user is divisible by both 2 and 3
# # A:
# n=int(input('Enter a number:'))
# if(n%2==0 and n%3==0):
#     print(n,"is divisible by both 2 and 3")
# else:
#     print(n,"is not divisible by both 2 and 3")

# # Q:Display "Hello" if a number entered by the user is the multiplication of 5,otherwise print "Bye"
# # A:
# n=int(input('Enter a number:'))
# if(n%5==0):
#     print('Hello')
# else:
#     print('Bye')


# # Q: Print last digit of a number is divisible by 3 or not
# # A:
# n=int(input('Enter a number:'))
# if(n%10%3==0):
#     print(n%10,'is divisible by 3')
# else:
#     print(n%10,'is not divisible by 3')