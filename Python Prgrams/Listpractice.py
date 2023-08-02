#list1 = ['Red', 'green', 'Blue', 'yellow', 'Orange']
'''for item in list1:
    print(item)'''
'''
i = 0
while i < len(list1):
    print(list1[i])
    i+=1'''



'''def increment(list):
    for i in range(0, len(list)):
        #5 is added to each element
        list[i]+=5
    print('refernce of list inside function',id(list))


list1= [10,20,30,40]
print("refernce of list in main", id(list1))
print(list1)

increment(list1)
print(list1)'''


mylist = [10,20,30,40,50]
while True:
    print("1.Append")
    print("2.Insert")
    print("3.Exit")

    choice = input("Enter your choice(1-3)")

    if choice == 1:
        element=int(input("enter the element"))
        mylist.append(element)
        print(element, "has appended")
        input("press any key to continue")
    elif choice == 2:
        index = int(input("Enter the index"))
        element=int(input("Enter the element"))
        mylist.insert(index, element)
        print(element, "has inserted")
        input("press any key to continue")
    elif choice == 3:
        break
    else:
        print("Invalid Number")



