# take something returns nothing
"""def add(a, b):
    c=a+b
    print("The Sum is", c)
    
add(32,21)
x,y=20, 45
add(x,y)"""
'''def add():
    a=int(input("Enter 1st number"))
    b=int(input("Enter 1st number"))
    c=a+b
    return c

print(add())'''
def add(a, b):
    c=a+b
    return c

print("Sum is ",add(10,40))
