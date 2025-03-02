# Syntax
# def function():
#     print('something')
# function()



# # Q: Create a function to add 2 numbers
# # A:
# def add():                                      # function declaration
#     a=int(input('Enter a number:'))
#     b=int(input('Enter a number:'))
#     print('sum =',a+b)                          # function definition
# add()                                           # function calling


# Global Variable and Local Variable
# ----------------------------------

# # 1. Global variable - variable declared outside the function. can call anywhere in the program
#
# num=10 # global variable
# def add():
#     a=11
#     b=12
#     print(a+b+num)   # num can call inside the function
# add()
# print(num)    # num can call outside the function


# # 2. Local variable - defined inside a function. cannot access outside the function
#
# def add():
#     a=11
#     b=12
#     print(a+b)
# add()
# print(a) # error

