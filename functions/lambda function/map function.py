# # Syntax
#
# x=list(map(lambda argument:expression,list_name))


# # Q: Find the square each element in the given list [1,2,3,4,5,6]
# # A:
# li=[1,2,3,4,5,6]
# x=list(map(lambda i:i**2,li))
# print(x)


# # Q: Find the square each element in the given list [1, 4, 9, 16, 25, 36]
# # A:
# li=[1, 4, 9, 16, 25, 36]
# x=list(map(lambda i:i**0.5,li))
# print(x)


# # Q: Using lambda map convert the first character of each string into uppercase
# # A:
# words=['welcome','hello','python']
# x=list(map(lambda i:i.capitalize(),words))
# print(x)


# # Q: Using lambda map print the reverse of each word in the list
# # A:
# words=['welcome','hello','python']
# x=list(map(lambda i:i[::-1],words))
# print(x)


# # Q: Create a list of numbers from 1 to 10 then take user input and generate list containing multiplications
# # of the input number
# # A:
# li=[1,2,3,4,5,6,7,8,9,10]
# n=int(input('Enter a number:'))
# x=list(map(lambda i:i*n,li))
# print(x)


# Mapping using multiple sequences
# --------------------------------

# Q: Add elements of two lists
# A:
