# front -  4 5 6 9 2 - Rear
# push - enqueue
# pop -  dequeue

myQueue= list()

def isEmpty(myQueue):
    if len(myQueue)==0:
        return True
    else:
        return False

def enqueue(myQueue, element):
    myQueue.append(element)


def dequeue(myQueue):
    if isEmpty(myQueue):
        return 'UnderFlow'
    else:
        return myQueue.pop(0)

def size(myQueue):
    return len(myQueue)

def peek(myQueue):
    if isEmpty(myQueue):
        print("Queue is Empty")
        return None
    else:
        return myQueue[0]
    
while True:
    print("IMPLEMENTAION of QUEUE")
    print("1.Enqueue")
    print("2.Size")
    print("3.peek")
    print("4.Dequeue")
    print("5.display")
    print("6.Exit")

    ch = int(input("Enter your choice(1-6)"))
    if ch == 1:
        item = int(input("Enter the element:"))
        enqueue(myQueue, item)
        print("Enqueue Successful")
        input("Press any key to continue")

    elif ch == 2:
        print("size:",size(myQueue))
        input("Press any key to continue")

    elif ch == 3:
        print(peek(myQueue))
        input("Press any key to continue")

    elif ch == 4:
        item = dequeue(myQueue)
        if item == 'UnderFlow':
            print("Queue is Empty")
        else:
            print(item, "dequeue successfull")
        input("Press any key to continue")
    elif ch == 6:
        break
    else:
        print("\nChhoti bachchi ho kya\n")

    
    
