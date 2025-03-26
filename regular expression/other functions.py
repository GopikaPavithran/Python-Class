import re

# # findall()
# # ---------
# str='this is my paragraph'
# find='a'
# x=re.findall(find,str)
# print(x)     # output - ['a', 'a', 'a']

# str='this is my paragraph'
# find='[a-z]+'
# x=re.findall(find,str)
# print(x)       # output - ['this', 'is', 'my', 'paragraph']

# str='my phone number is 7890639424'
# find1='[\d]+'    # for numbers
# find2='[\w]+'    # for words (except space,numbers included)
# find3='[\s]'     # for space
# find4='[\D]'     # except digits
# a=re.findall(find1,str)
# b=re.findall(find2,str)
# c=re.findall(find3,str)
# d=re.findall(find4,str)
# print(a)
# print(b)
# print(c)
# print(d)
#
# # output
# # ['7890639424']
# # ['my', 'phone', 'number', 'is', '7890639424']
# # [' ', ' ', ' ', ' ']
# # ['m', 'y', ' ', 'p', 'h', 'o', 'n', 'e', ' ', 'n', 'u', 'm', 'b', 'e', 'r', ' ', 'i', 's', ' ']


# # search()
# # --------
# para='hello welcome to python'
# find='python'
# search=re.search(find,para)
# print(search)   # output - <re.Match object; span=(17, 23), match='python'>
#                                                 # (17-23 : index)
# if search:
#     print('Found')
# else:
#     print('Not Found')


# # split()
# # -------
# txt='varun and arun are students'
# x=re.split('\s',txt)
# print(x)     # output - ['varun', 'and', 'arun', 'are', 'students']


# sub()
# -----
txt='varun and arun are students'
x=re.sub('\s','#',txt)
print(x)       # output - varun#and#arun#are#students