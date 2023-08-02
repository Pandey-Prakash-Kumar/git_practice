'''Write a program with a user defined 
function to count the number of times a 
character (passed as argument) occurs in 
the given string'''

'''def charCount(ch, st):
    count = 0
    for character in st:
        if character == ch:
            count+=1

    return count

str = input("Enter any string:")


print(charCount('a', str))'''

'''Write a program with a user defined 
function with string as a parameter which 
replaces all vowels in the string with '*'.'''

'''def replaceVowel(st):
    newstr = ''
    for char in st:
        if char == "aeiouAEIOU":
            newstr += '*'
        else:
            newstr += char


    return newstr

str = input("Enter a string")
st = replaceVowel(str)
print(st)
'''


'''Write a program to input a string from 
the user and print it in the reverse order 
without creating a new string'''

str = input("enter a string")
for i in range(-1, -len(str)-1, -1):
    print(str[i], end ='')

''' Write a program which reverses a string 
passed as parameter and stores the 
reversed string in a new string. Use a user 
defined function for reversing the string.'''

'''Write a program using a user defined 
function to check if a string is a palindrome 
or not. (A string is called palindrome if it 
reads same backwards as forward. For 
example, Kanak is a palindrome.) 

'''
