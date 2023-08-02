stak = list()
def isEmpty(stak):
    if len(stak) == 0:
        return True
    else:
        return False

def opPush(stak,element):
    stak.append(element)

def size(stak):
    return len(stak)

def top(stak):
    if isEmpty(stak):
        print('stack is Empty')
        return None
    else:
        x = len(stak)
        element = stak[x-1]
        return element

def opPop(stak):
    if isEmpty(stak):
        print("Underflow")
        return None
    else:
        return stak.pop()
    
def display(stak):
    x = len(stak)
    print("The elements of Stack are :")
    for i in range(x-1, -1, -1):
        print(stak[i])

while True:
    print("IMPLEMENTAION of STACK")
    print("1.Push")
    print("2.Size")
    print("3.top")
    print("4.Pop")
    print("5.display")
    print("6.Exit")

    ch = int(input("Enter your choice(1-6)"))
    if ch == 1:
        item = int(input("Enter the element:"))
        opPush(stak,item)
        print("pushed successfully")
        input('Press any key to continue')

    elif ch == 2:
        print("Size is ",size(stak))
        input('Press any key to continue')

    elif ch == 3:
        item = top(stak)
        if item == None:
            print('Underflow')
        else:
            print("top element ", item)
        input('Press any key to continue')

    elif ch == 4:
        item = opPop(stak)
        if item == None:
            print("Underflow")
        else:
            print(item," is popped")
        input('Press any key to continue')

    elif ch == 5:
        display(stak)
        input('Press any key to continue')
    elif ch == 6:
        break
    else:
        print("Chhoti bachhi ho kya")
        input('Press any key to continue')



