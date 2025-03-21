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

# from multipledispatch import dispatch
# class Math:
#     @dispatch(int,int)
#     def sum(self,a,b):
#         print(a+b)
#     @dispatch(int,int,int)
#     def sum(self,a,b,c):
#         print(a+b+c)
# obj=Math()
# obj.sum(6,3,2)
# obj.sum(1,3)


# # Q: Create product functions
# # product(1,2)
# # product(1,2,3)
# # product(1.5,2.2)
# # product(1.3,2.1,3.8)
# # A:
# from multipledispatch import dispatch
# class Math:
#     @dispatch(int,int)
#     def product(self,a,b):
#         print(a*b)
#     @dispatch(int,int,int)
#     def product(self,a,b,c):
#         print(a*b*c)
#     @dispatch(float,float)
#     def product(self,a,b):
#         print(a*b)
#     @dispatch(float,float,float)
#     def product(self,a,b,c):
#         print(a*b*c)
# obj=Math()
# obj.product(1,2)
# obj.product(1,2,3)
# obj.product(1.5,2.2)
# obj.product(1.3,2.1,3.8)


# Q: Create length functions
# length('abc')
# length([1,2,3,4])
# length({'a','b'})
# length({'Name':'Alex','Age':22})
# length(('a','b','c'))
# A:
from multipledispatch import dispatch
class Length:
    l=0
    @dispatch(str)
    def length(self,st):
        self.l=0  # Reset length for each call
        for i in st:
            self.l+=1
        print(self.l)
    @dispatch(list)
    def length(self,li):
        self.l=0
        for i in li:
            self.l+=1
        print(self.l)
    @dispatch(set)
    def length(self,se):
        self.l=0
        for i in se:
            self.l+=1
        print(self.l)
    @dispatch(dict)
    def length(self,di):
        self.l=0
        for i in di:
            self.l+=1
        print(self.l)
    @dispatch(tuple)
    def length(self,tu):
        self.l=0
        for i in tu:
            self.l+=1
        print(self.l)
obj=Length()
obj.length('abc')
obj.length([1,2,3,4])
obj.length({'a','b'})
obj.length({'Name':'Alex','Age':22})
obj.length(('a','b','c'))
