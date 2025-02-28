# s={'a','c',1,8.4}
# print(type(s))


# Methods
# -------

# # 1.add()              # to add new element
# s={'a','c',1,8.4}
# s.add(5)
# print(s)


# # 2.discard()            # to remove an element.does not show error if element not found
# s={'a','c',1,8.4}
# s.discard('b')
# print(s)


# # 3.remove()               # to remove an element.show error if element not found
# s={'a','c',1,8.4}
# s.remove(1)
# print(s)


# # 4.pop()                    # removes a random element
# s={'a','c',1,8.4,78}
# s.pop()
# print(s)


# # 5.symmetric_difference()   # returns a new set containing the elements that are in either of the sets
# x={1,2,3,4}
# y={1,2,5,6}
# z=x.symmetric_difference(y)
# print(z)

# # output - {3, 4, 5, 6}

# # we can use set1 ^ set2 (operator) instead of set1.symmetric_difference(set2)
# x={1,2,3,4}
# y={1,2,5,6}
# z=x^y
# print(z)


# # 6.symmetric_difference_update()   # it does not return a new set. It updates the existing set with the symmetric difference.
# x={1,2,3,4}
# y={1,2,5,6}
# x.symmetric_difference_update(y)
# print(x)
#
# # output - {3, 4, 5, 6}
#
# # we can use set1 ^= set2 instead of set1.symmetric_difference_update(set2)
# x={1,2,3,4}
# y={1,2,5,6}
# x^=y
# print(x)


# # 7.intersection()          # returns a new set containing only the elements that are common to both sets
# x={1,2,3,4}
# y={1,2,5,6}
# z=x.intersection(y)
# print(z)
#
# # # output - {1, 2}
#
#  # set1 & set2 or set1.intersection(set2)
# x={1,2,3,4}
# y={1,2,5,6}
# z=x&y
# print(z)


# # 8. intersection_update()       # updates the set to contain only the elements that are common to both sets.
# x={1,2,3,4}
# y={1,2,5,6}
# x.intersection_update(y)
# print(x)

# # output - {1, 2}

# # set1.intersection_update(set2) or set1 &= set2
# x={1,2,3,4}
# y={1,2,5,6}
# x&=y
# print(x)