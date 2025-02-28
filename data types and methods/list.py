# li=['a','b',1,2,1.3]
# print(type(li))


# # Q: Find length of a list
# # A:
# print(len(li))


# # Methods
# # -------
#
# # 1.append()              # add new element in the end of the list
# li.append('c')
# print(li)


# # 2.insert()              # add an element using index position
# li.insert(2,'hi')
# print(li)


# # 3.extend()              # add a list of elements
# li.extend([4,5,6])
# print(li)


# # 4.pop()
# li.pop()                  # delete last element
# print(li)
#
# li.pop(1)
# print(li)                 # delete element using index


# # 5.remove()              # remove an element using its name
# li.remove(1)
# print(li)


# # 6.reverse()             # reverse the list
# li.reverse()
# print(li)


# # 7.sort()                # to sort in an order
# l=[3,6,8,5,1]
# l.sort()
# print(l)


# # Q: Sort a list of alphabets
# # A:
# li=['r','t','w','e','q','f','a']
# li.sort()
# print(li)


# # Q: Sort the list ['A','a','B','C','b','c']
# # A:
# li=['A','a','B','C','b','c']
# li.sort()
# print(li)


# # To Sort In Descending Order
# # ---------------------------
#
# list.sort()
# list.reverse()
# print(list)
#
#               # OR
#
# list.sort(reverse=True)
# print(list)


# # Q: Sort in descending order [55,23,6,77,89,1,33,43,20]
# # A:
# li=[55,23,6,77,89,1,33,43,20]
# li.sort(reverse=True)
# print(li)


# List Iteration
# --------------

# for i in li:
#     print(i)


# # Q: Without using len() find length of a list
# # A:
# li=[3,5,2,'d','h','hi',9]
# c=0
# for i in li:
#     c+=1
# print('Length of list=',c)


# # Q: Find the sum of elements in the given list [100,200,300,400,500]
# # A:
# li=[100,200,300,400,500]
# s=0
# for i in li:
#     s+=i
# print('Sum =',s)


# # Q: without using slicing and reverse(), reverse a list
# # A:
# rev=[]
# li=[4,6,7,2,5,'a','g']
# for i in li:
#     if i not in rev:
#         rev.insert(0,i)
# print(rev)
#
#               # OR
#
# rev = []
# li = [4, 6, 7, 2, 5,'a','g']
# last=len(li)-1
# for i in range(last,-1,-1):
#     rev.append(li[i])
# print(rev)


# # Q: To remove duplicate elements from the given list ['a','b','c','a','c']
# # A:
# l1=['a','b','c','a','c']
# l2=[]
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)


# # Q: Count the number of alphabets and digits in the given list [1,2,3,'a','b','c','d']
# # A:
# li=[1,2,3,'a','b','c','d']
# ac=0
# dc=0
# for i in li:
#     if str(i).isalpha():           # converts to string. because isalpha(),isnumeric() etc.. are only applicable in string
#         ac+=1
#     elif str(i).isnumeric():
#         dc+=1
# print('Count of alphabets:',ac)
# print('Count of digits:',dc)


# # Q: Create a list using user input
# # A:
# li=[]
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     e=input('Enter the element:')
#     li.append(e)
# print(li)


# # Q: Create a list like ['a','b','c',1,2,3]
# # A:
# li=[]
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     e=input('Enter the element:')
#     if(e.isalpha()):
#         li.append(str(e))
#     elif(e.isnumeric()):
#         li.append(int(e))
# print(li)


# # Q: Create a list of numbers input by the user and generate a new list with its square value
# # A:
# li=[]
# sq=[]
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     e=input('Enter the element:')
#     li.append(int(e))                     # Use int() when appending the number element into the list while using user input
#     sq.append(int(e)**2)                  #  because input function always take element as string
# print(li)
# print(sq)


# # Q: Create 2 list of string
# #           ['hello','hi'] - original
# #           ['olleh','ih'] - reverse of string
# # A:
# li=[]
# rev=[]
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     e=input('Enter the string:')
#     li.append(e)
# print(li)
# for i in li:
#     rev.append(i[::-1])
# print(rev)


# # Q: Find the largest element in the list
# # A:
#
# # using sort()

# li=[]
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     e=input('Enter the element:')
#     li.append(int(e))
# li.sort(reverse=True)
# print(li[0])
#
#             # OR
#
# li=[]
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     e=input('Enter the element:')
#     li.append(int(e))
# li.sort()
# print(li[len(li)-1])


# # without using function
#
# li=[]
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     e=input('Enter the element:')
#     li.append(int(e))
# num=li[0]
# for i in li:
#     if i>num:
#         num=i
# print(num)


# # when elements are strings
#
# li=['hi','hello','welcome',]
# length=0
# word=''
# for i in li:
#     if len(i)>length:
#         length=len(i)
#         word=i
# print(word)


# # Q: Generate a list of numbers and also print the smallest number in the list
# # A:
# li=[]
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     e=input('Enter the element:')
#     li.append(int(e))
# print(li)
# li.sort()
# print('Smallest Number -',li[0])
