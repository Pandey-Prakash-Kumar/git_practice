#. 1. Write a python script to add comments and print “Learning Python” on screen.
#print("Learning Python")

'''2. Write a python script to add multi line comments and print values of four 
variables, each in a new line. Variable contains any values.'''

'''x=78
bl = True
f=3.45
name = "Prakash"
print( " ", x, "\n",bl, "\n", f, "\n", name)'''

'''3. Write a python script to print types of variables. Create 5 variables each of them
containing different types of data. (like 35, True, “Prakash”,5.46, 3+4j, etc)
'''


'''n=35
b = True
name = "Prakash"
f= 5.46
c=3+4j
print(type(n))
print(type(b))
print(type(name))
print(type(f))
print(type(c))'''

''' 4. . Write a python script to print the id of two variables containing the same integer
values.
'''
'''x = 98
y = 98
print(id(x))
print(id(y))'''
'''Create four variables in a Python script and assign values of different data types to
them. Write a Python script to print value, its type and id of each variable'''

'''n=35
b = True
name = "Prakash"
f= 5.46
c=3+4j
print(n, type(n), id(n))'''

#Write a python script to print all the keywords

'''import keywords
print(keywords.kwlist)'''

'''Create two Python files A0.py and A1.py. Create a variable in A1.py and assign 
some value to it. Write a python script to import A1 module in A0 and print value of the
variable created in A0.py'''

'''import A1
print(A1.var1)'''

#9. Name the keywords, used as data in the Python script.
#True False None
'''10. Write a python script to display the current date and time. First create variables 
to store date and time, then display date and time in proper format (like: 13-8-2022 
and 9:00 PM)'''

'''from datetime import datetime
a=datetime.now()
print(a)

dt= a.strftime("%d/%m/%Y %H:%M:%S")
print(dt)'''
#11. Write a python script to convert a number into str type.

'''x = 56
print(x, type(x))
y = str(x)
print(y, type(y))'''

#12. Write a python script to print Unicode of the character ‘m’

#print(ord(u'र'))

#13. Write a python script to print character representation of a given unicode 100

#print(chr(2358))

#14. Write a python script to print any number and its binary equivalent


#print(hex(234))

'''Write a python script to take your name as input from the user and then 
print it'''

#name = input("Enter your Name:")
#print("Hi, ", name)

#Write a python script to take input from the user. Input must be a number.1. Write a python script to take your name as input from the user and then print it
'''n = int(input("Enter a number:"))
print("The number is ", n)'''

'''3. Write a python script which takes two numbers from the user, then 
calculate their sum and display the result'''
'''x = int(input("First Number = "))
y = int(input("Second Number = "))
sum = x+y
print("Sum =", sum)'''

'''4. Write a python script which takes the radius from the user and display area 
of a circle'''
'''r = float(input("Enter radius of circle:"))
area = 3.14 * r * r
print("Area of Circle = ", area)'''

x = int(input("Enter a number:"))
print(x**2)

        
        































