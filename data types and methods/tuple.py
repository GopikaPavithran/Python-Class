# t=('a','g',5.6,3,22,'r')
# print(type(t))


# # using len() in tuple
# t=('a','g',5.6,3,22,'r')
# print(len(t))


# # using count() in tuple
# t=(1,5,8,3,5,9,4)
# print(t.count(5))


# # index()
# t=(1,5,8,3,5,9,4)
# print(t.index(8))


# # Tuple Iteration
# t=('e','d','t','g')
# for i in t:
#     print(i)


# # Element Accessing
# t=('e','r','c','a','h')
# print(t[3])


# # Slicing
# t=('e','r','c','a','h','d','t','g')
# print(t[2:6])


# # Tuple Reversing
# t=('e','r','c','a','h','d','t','g')
# print(t[::-1])


# # Q: Add a new element 6 to the end of the tuple (1,2,3,4,5)
# # A:
# t=(1,2,3,4,5)
# l=list(t)                 # convert into list, because tuple is immutable
# l.append(6)
# t=tuple(l)
# print(t)

             # OR

# # using tuple concatenation
# t1=(1,2,3,4,5)
# t2=(6,)             # have to add a comma, otherwise python will not recognize the variable as tuple
# t3=t1+t2
# print(t3)
