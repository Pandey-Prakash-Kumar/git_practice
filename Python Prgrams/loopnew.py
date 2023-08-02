#1. Write a python script to calculate sum of first N natural numbers
'''sum = 0
n = int(input("Enter a no.-"))
for i in range(1, n+1):
    sum = sum + i
    
print("Sum of first",n,"natural numbers = ",sum)'''

#2. Write a python script to calculate sum of squares of first N natural number
'''
num = int(input("ENter a number:"))
sum = 0'''
'''for i in range(1, num+1):
    sum = sum+(i**2)
print(sum)'''
'''i = 1
while i<=num:
    sum = sum + (i**2)
    i+=1
print(sum)'''


#3. Write a python script to calculate sum of cubes of first N natural numbers
'''n = int(input("enter a number:"))
sum = 0
for i in range(1,n+1):
    sum = sum+(i**3)

print(sum)'''

#4. Write a python script to calculate sum of first N odd natural numbers

'''n = int(input("Enter a number:"))
sum = 0
for i in range(1,n*2,2):
    sum = sum + i 
print(sum)'''

#5. Write a python script to calculate sum of first N even natural numbers

'''num = int(input("Enter a number:"))
sum = 0
for i in range(2, num*2+1, 2):
    sum = sum +i
print(sum)'''

#6. Write a python script to calculate factorial of a given number
'''x = int(input("Enter a number:"))
fact = 1
for i in range(x, 0, -1):
    fact = fact*i
print(fact)
'''

#7. Write a python script to count digits in a given number
'''n = int(input("Enter a number"))
count_digit = len(str(n))
print(count_digit)
'''
#8. Write a python script to calculate sum of digits of a given number

'''n = int(input("Enter a number:"))
num_str = str(n)
sum = 0
for d in num_str:
    sum = sum + int(d)
print(sum)
'''

#9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
'''dec = int(input("Enter the number"))
if dec ==0:
    print('0')
else:
    bin_str = ' '
    while dec>0:
        remainder = dec%2
        bin_str = str(remainder) + bin_str
        dec//=2

    print(bin_str)'''


#10
'''dec = int(input("Enter a number:"))
oct_str = ' '
if dec == 0:
    print('0')
else:
    while dec>0:
        remainder = dec%8
        oct_str = str(remainder)+oct_str
        dec//=8
    print(oct_str)'''

print(bin(12))


 


  



   

