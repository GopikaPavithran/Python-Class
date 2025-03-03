# # Syntax
# x=reduce(lambda a,b:a+b,li)


from functools import reduce

# # Q: Find sum of the given list using lambda reduce
# # A:
# li=[1,2,3,4,5,6]
# x=reduce(lambda a,b:a+b,li)
# print(x)


# # Q: Find the minimum value, maximum value and product of the given list [100,200,...500]
# # A:
# li=[100,200,300,400,500]
# min=reduce(lambda a,b:a if a<b else b,li)
# print(min)

# max=reduce(lambda a,b:a if a>b else b,li)
# print(max)

# product=reduce(lambda a,b:a*b,li)
# print(product)
