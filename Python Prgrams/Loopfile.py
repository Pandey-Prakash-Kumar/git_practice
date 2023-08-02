#1. Write a python script to reverse a number
'''num = int(input("Enter a number:"))
num_str= str(num)
r_str= num_str[ : :-1]
r_num = int(r_str)
print(int(r_num))'''

#2. Write a python script to check whether a given number is Prime or not

'''n = int(input("Enter a number:"))
flag = 0
for i in range(2,n):
    if n%i == 0:
        flag = 1
        break
if flag == 0:
    print(n, "is prime")
else:
    print(n,"is not prime") '''

#3. Write a python script to print all Prime numbers under 100

'''def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True

for i in range(1,100):
    if isPrime(i) == True:
        print(i)'''

#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
'''def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True
print("Enter the range:")
n1,n2 = int(input()),int(input())
print("The primes between",n1, "and",n2, "are:")
for i in range(n1, n2+1):
    if isPrime(i) == True:
        print(i)'''

#.5 Write a python script to find next prime number of a given number
def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True

n = int(input("Enter a number:"))
for i in range(n+1,n+100):
    if isPrime(i) == True:
        print("Next Prime Number is",i)
        break
    
    






