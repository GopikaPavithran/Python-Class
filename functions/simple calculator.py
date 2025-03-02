def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b


print('SIMPLE CALCULATOR')
print('-----------------')
print('Choices')
print('~~~~~~~')
print('1 for Addition \n2 for Subtraction \n3 for Division \n4 for Multiplication')
c=int(input('Enter your choice:'))
if c in [1,2,3,4]:
    a=int(input('Enter first number:'))
    b=int(input('Enter second number:'))
    if c==1:
        print(a,'+',b,'=',add(a,b))
    elif c==2:
        print(a, '-', b, '=',sub(a, b))
    elif c==3:
        print(a, '/', b, '=', div(a, b))
    else:
        print(a, 'x', b, '=', mul(a, b))
else:
    print('Please Enter a Valid Choice')


