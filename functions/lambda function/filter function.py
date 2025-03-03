# # Syntax
#
# x=list(filter(lambda argument: expression,list_name))


# # Q: Filter out even numbers from the given list [1,2,3,4]
# # A:
# li=[1,2,3,4]
# even=list(filter(lambda i:i%2==0,li))
# print(even)


# # Q: Filter out even numbers from the given list [1,2,3,4,5,6]
# # A:
# li=[1,2,3,4,5,6]
# x=list(filter(lambda i:i%2==1,li))
# print(x)


# # Q: Filter out positive numbers from the given list [1,-1,2,-2,3,-3]
# # A:
# li=[1,-1,2,-2,3,-3]
# x=list(filter(lambda i:i>0,li))
# print(x)


# # Q: Filter out alphabets from the given list [1,2,'a',3,'b']
# # A:
# li=[1,2,'a',3,'b']
# li=str(li)
# x=list(filter(lambda i:i.isalpha(),li))
# print(x)


# # Q: Filter the numbers which are divisible by 2 but not by 3 from given list [1,2,3,4,5,6,7,8]
# # A:
# li=[1,2,3,4,5,6,7,8]
# x=list(filter(lambda i:i%2==0 and i%3!=0,li))
# print(x)


# Q: Create a function using def and pass a list of alphabets as an argument and using lambda filter out vowels
# and return the list of vowels
# A:
def vowel(n):
    x=list(filter(lambda i:i in 'aeiou',n))
    return x
print(vowel(['o','r','w','a','f','i']))