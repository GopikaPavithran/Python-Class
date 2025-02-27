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