# # Method overriding with single inheritance
#
# class A:
#     def fun1(self):
#         print('Hello...')
# class B(A):         # requires inheritance
#     def fun1(self):
#         print('Hai...')
# obj=B()
# obj.fun1()
# # fun1 of B that overrides fun1 of A
#
#
# # To access fun1 of parent class - super().function_name()
# class A:
#     def fun1(self):
#         print('Hello...')
# class B(A):
#     def fun1(self):
#         print('Hai...')
#         super().fun1()   # accessing parent class's function
# obj=B()
# obj.fun1()
#
#
# # Another example for overriding
# class Math:
#     def sum(self,a,b):
#         print(a+b)
# class Childmath:
#     def sum(self,a,b):
#         print(a*b)
# obj=Childmath()
# obj.sum(4,5)



# # Overriding with multiple inheritance
#
# class Mathparent1:
#     def sum(self,a,b):
#         print(a+b)
# class Mathparent2:
#     def product(self,a,b):
#         print(a*b)
# class Childmath(Mathparent1,Mathparent2):
#     def sum(self,a,b):
#         print(a-b)
#     def product(self,a,b):
#         print(a/b)
# obj=Childmath()
# obj.sum(7,4)
# obj.product(20,5)
#
#
# # To access parent functions
# class Mathparent1:
#     def sum(self,a,b):
#         print(a+b)
# class Mathparent2:
#     def product(self,a,b):
#         print(a*b)
# class Childmath(Mathparent1,Mathparent2):
#     def sum(self,a,b):
#         print(a-b)
#     def product(self,a,b):
#         print(a/b)
#         super().sum(5,3)
#         super().product(6,3)
# obj=Childmath()
# obj.sum(7,4)
# obj.product(20,5)


# # Overriding with multilevel inheritance
#
# class A:
#     def display(self):
#         print('Function of A')
# class B(A):
#     def display(self):
#         print('Function of B overrides function of A')
# class C(B):
#     def display(self):
#         print('Function of C overrides function of B')
# obj=C()
# obj.display()
#
#
# # Accessing parent functions
# class A:
#     def display(self):
#         print('Function of A')
# class B(A):
#     def display(self):
#         print('Function of B overrides function of A')
# class C(B):
#     def display(self):
#         print('Function of C overrides function of B')
#         B().display()
#         A().display()
# obj=C()
# obj.display()


# # Overriding with hierarchical inheritance
#
# class Grandfather:
#     def property(self):
#         print('Grand father owns complete land')
# class Father(Grandfather):
#     def property(self):
#         print('Father owns 50% of the land')
# class Son(Grandfather):
#     def property(self):
#         print('Son owns 25% of the land')
# dad=Father()
# dad.property()
# kid=Son()
# kid.property()



