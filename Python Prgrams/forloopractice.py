#1. Write a python script to print the first 10 multiples of 5.
'''for n in range(1, 11):
    print(5*n)'''

#2. Write a python script to print first 10 multiples of N
'''num = int(input("Enter a number:"))
for i in range(1,11):
    print(num*i)'''

#3. Write a python script to print first M multiples of N.
'''n = int(input("Enter a number:"))
m = int(input("How many multiples?"))
for i in range(1,m+1):
    print(n*i)'''

#4. Write a python script to print the first 10 multiples of N in reverse order.
'''n = int(input("Enter a number:"))
for i in range(10,0,-1):
    print(n*i)'''

#5. Write a python script to print table of user’s choice
'''n = int(input("Enter a number:"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)'''

#6. Write a python script to print first N even natural numbers.
'''num = int(input("Enter a number:"))
for i in range(2,num*2+1,2):
    print(i)'''

#7. Write a python script to print first N odd natural numbers
'''n = int(input("Enter a no.:"))
for i in range(1,n*2,2):
    print(i)'''

#8. Write a python script to print squares of first N natural numbers.

'''n = int(input("Enter a no:-"))
for c in range(1,n+1):
    print(c**2)'''

#9. Write a python script to print cubes of first N natural numbers.

'''n = int(input("Enter a no.-"))
for i in range(1,n+1):
    print(i**3)'''

#10. Write a python script to display all prime numbers within a range.
# range
'''start = 15
end = 45'''
def isprime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True
    

start = 15
end = 45
for i in range(15,45):
    if isprime(i):
        print(i)

        
    

            
        

