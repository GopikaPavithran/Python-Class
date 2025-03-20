# class Math:
#     def sum(self,a,b):
#         print(a+b)
#     def sum(self,a,b,c):
#         print(a+b+c)
# obj=Math()
# obj.sum(6,3,2)
# obj.sum(1,3)   # Execution will result in a positional argument error
#
# # In the above code,we have defined two add functions, but we can only use the second add function, as python does not support
# # method overloading directly
#
# # multipledispatch : a method that is used for achieve method overloading in python.
# # It is a package needs to be installed (pip install multipledispatch)
#
# # Python decorator - a design pattern in Python that allows a user to add new functionality to an existing object without modifying
# # its structure.
#
# # @dispatch is a decorator that enables multiple dispatch in Python (@ symbol is essential at the beginning of a decorator's name)

from multipledispatch import dispatch
class Math:
    @dispatch(int,int)
    def sum(self,a,b):
        print(a+b)
    @dispatch(int,int,int)
    def sum(self,a,b,c):
        print(a+b+c)
obj=Math()
obj.sum(6,3,2)
obj.sum(1,3)