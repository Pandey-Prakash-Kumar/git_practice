#6. Write a python script to print first N prime numbers

'''def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True
N = int(input('Enter a number'))
count = 1
n = 2
while count <= N:
    if isPrime(n):
        print(n)
        count+=1
    n+=1'''

# Write a python script to check whether a given pair of numbers are co-Prime
#numbers or not.
'''
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def are_coprime(a,b):
    return gcd(a,b)==1


print("Enter the pair of number:")
n1,n2 = int(input()),int(input())
if are_coprime(n1,n2):
    print("Yes. They are co-prime")
else:
    print("No. They are not coprime")'''

# Write a python script to print first N terms of a Fibonacci series

def fibanacci_series(N):
    series = []
    a, b =0, 1
    for i in range(N):
        series.append(a)
        a,b = b, a+b
    return series

num = int(input("Enter a number"))
fs = print(fibanacci_series(num))

# 9. Write a python script to calculate LCM of two numbers
def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)


print("Enter two number:")
n1,n2 = int(input()),int(input())
print("LCM =",lcm(n1,n2))