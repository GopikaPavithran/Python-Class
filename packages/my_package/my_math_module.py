import math

# Addition
def add(a,b):
    return a+b

# Area of circle
def cir_area(r):
    return math.pi*(r**2)

# Reverse of number
def revese(n):
    s=str(n)
    return int(s[::-1])

# Product
def product(*n):
    p = 1
    for i in n:
        p*=i
    return p

# Smallest
def smallest(*n):
    f=n[0]
    for i in n:
        if i<f:
            f=i
    return f

# Largest
def largest(*n):
    f=n[0]
    for i in n:
        if i>f:
            f=i
    return f
