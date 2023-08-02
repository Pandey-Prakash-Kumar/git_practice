#1. Write a python script to check whether a given number is positive or non-positive
"""num = int(input("Enter a number:"))
if num>0:
    print("Number is positive")
else:
    print("Number is non posituve")
"""
#2. Write a python script to check whether a given number is divisible by 5 or not
'''n = int(input("Enter a number:"))
if n%5==0:
    print(n,"is divisble by 5")
else:
    print(n, "is not divisble by 5")'''

#3. Write a python script to check whether a given number is even or odd
'''num1 = int(input("Enter a number:"))
if num1%2==0:
    print("Number is Even")
else:
    print("Number is Odd")'''

#4. Write a python script to print greater between two numbers. Print number only once
#even if the numbers are the same.

'''num1 = int(input("Enter 1st Number:"))
num2 = int(input("Enter 2nd number:"))
if num1>num2:
    print(num1, "is greater than", num2)
elif num1<num2:
    print(num2, "is greater than", num1)
else:
    print("Number is equal",num1,num2)'''

#5. Write a python script to print two given words in dictionary order
# A = 65    B = 66
'''word1=input("Enter 1st Word:")
word2=input("Enter 2nd word:")
if word1<word2:
    print(word1)
    print(word2,"\n")
else:
    print(word2)
    print(word1,"\n")'''
#6. Write a python script to check whether a given number is a three digit number or not.
'''x = int(input("Enter a number:"))
if x >=100 and x<=999:
    print("Three digit Number")
else:
    print("Not three digit number")'''

#7. Write a python script to check whether a given number is positive, negative or zero.
'''n = int(input("Enter the number:"))
if n>0:
    print("Positive")
elif(n<0):
    print("Negative")
else:
    print("Zero")
'''
#8. Write a python script to check whether a given quadratic equation has two real &
#distinct roots, real & equal roots or imaginary roots
'''print("Enter a,b,c of Quadratic Equation:")
a = int(input("a = "))
b = int(input("b = "))
c = int (input("c = "))
d = (b**2)-(4*a*c)
if d>0:
    print("real & distinct roots")
elif d==0:
    print("real & equal roots")
else:
    print("imaginary roots")
'''

#9. Write a python script to check whether a given year is a leap year or not.

y = int(input("Enter Year:"))
if y%4 ==0:
    if y%100==0:
        if y%400 ==0:
            print("leap Year")
        else:
            print("Not Leap year")
    else:
        print("leap Year")      
else:
    print("Not Leap year")