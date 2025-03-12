# #Syntax
#
# class Abc:
#     def function(self):
#         print('New Class')
# obj=Abc()          # reference variable or reference object
# obj.function()


# Q: Create a class math with functions addition,subtraction,multiplication,division,remainder
# A:
class Math:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def div(self,a,b):
        print(a/b)
    def mul(self,a,b):
        print(a*b)
    def rem(self,a,b):
        print(a%b)

obj=Math()
obj.add(5,7)
obj.sub(8,4)
obj.div(120,5)
obj.mul(43,2)
obj.rem(20,3)