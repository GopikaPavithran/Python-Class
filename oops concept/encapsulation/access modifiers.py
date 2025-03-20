# # Public access modifiers
#
# class Employee:
#     def __init__(self,name,salary,phone):
#         # public datas
#         self.n=name
#         self.s=salary
#         self.p=phone
#     def display(self):  # public function
#         print(self.n)
#         print(self.s)
#         print(self.p)
# obj=Employee('Gopika',100000,536013467)
# obj.display()   # public accessing of function
# print(obj.n)    # public accessing of variables
# print(obj.s)
# print(obj.p)


# # Private access modifiers
#
# class Employee:
#     def __init__(self,name,salary):
#         self.n=name  # public data
#         self.__s=salary  # private data
#     def __display(self):  # private function
#         print(self.n)
#         print(self.__s)
# obj=Employee('Gopika',100000)
# print(obj.n)
# print(obj.__s)      # it shows an error.
# obj.__display()     # here we cannot access the private variable and private function outside the class


# Name mangling method : a method that is used to access private data members and methods outside the class
# Syntax :
# _classname__datamember


# Q: Access private data using name mangling method
# A:
class Employee:
    def __init__(self,name,salary):
        self.n=name  # public data
        self.__s=salary  # private data
    def __display(self):  # private function
        print(self.n)
        print(self.__s)
obj=Employee('Gopika',100000)
print(obj.n)
print(obj._Employee__s)
obj._Employee__display()
