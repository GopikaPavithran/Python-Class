# d={'Name':'Gopika',
#      'Phone':1224545}
# print(type(d))


# # Methods
# #--------
#
# # 1.keys()                   # to access keys
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Location':'Kasargod'


# # 2.values()                   # to access values
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Location':'Kasargod'
#    }
# print(d.values())


# # 3.get()                        # return value of a specific key
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Location':'Kasargod'
#    }
# print(d.get('Name'))


# # 4.pop()                          # remove element with specific key
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Location':'Kasargod'
#    }
# d.pop('Phone')
# print(d)


# # 5.popitem()                        # remove last key value pair
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Location':'Kasargod'
#    }
# d.popitem()
# print(d)


# # 6.update()                           # add a new pair or update value of a particular key
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Location':'Kasargod'
#    }
# d.update({'Age': 22})
# print(d)


# # 7.items()                              # get both keys and values
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Location':'Kasargod'
#    }
# print(d.get('Location'))


# # Q: Create an empty dictionary and add key value pairs in to the dictionary using user input
# # A:
# di={}
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     k=input('Enter the key:')
#     v=input('Enter the value:')
#     if v.isnumeric():
#         di.update({k:int(v)})
#     else:
#         di.update({k:v})
# print(di)


# # Q: Without using a function update a data in dictionary
# # A:
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Age':20
#    }
# d['Age']=22
# print(d)


# # Dictionary Iteration
# # --------------------
#
# d={'Name':'Gopika',
#    'Phone':1224545,
#    'Location':'Kasargod'
#    }
# for i in d:                    # iterate keys only
#     print(i)

# for i in d.values():           # iterate values only
#     print(i)

# for i,j in d.items():          # iterate both keys and values
#     print(i,j)


# # Q: Create an empty dictionary and pass key value pairs using user input. key should be a word and the value
# # should be the length of the word.
# # A:
# di={}
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     k=input('Enter a word:')
#     v=len(k)
#     di.update({k: v})
# print(di)


# # Q: Create an empty dictionary and pass key value pairs using user input. key should be a word and the value
# # should be the reverse
# # A:
# di={}
# n=int(input('Enter the number of elements to insert:'))
# for i in range(n):
#     k=input('Enter a word:')
#     v=k[::-1]
#     di.update({k: v})
# print(di)


# # Q: Input a string from the user and create a dictionary with the count of each character in the string
# # A:
# di={}
# a=input('Enter a string:')
# for i in a:
#     k=i
#     v=a.count(i)
#     di.update({k:v})
# print(di)


# # Q: Sort the dictionary {'b':3,'a':2,'c':4,'d':1,'e':4}
# # A:
# di={'b':3,'a':2,'c':4,'d':1,'e':4}
# l=list(di)
# l.sort()
# new={}
# for i in l:
#     new.update({i:di.get(i)})
# print(new)



#