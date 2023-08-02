def replaceVowel(st):
    newstr = ''
    for char in st:
        if char == 'aeiouAEIOU':
            newstr += '*'
        else:
            newstr += char
    return newstr

str = input("Enter a string")
st = replaceVowel(str)
print(st)
