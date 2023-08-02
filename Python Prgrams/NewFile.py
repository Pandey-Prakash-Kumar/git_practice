def writing(FileName, text):
    with open(FileName, 'w') as f:
        f.write(text)

def append(FileName, text):
    with open(FileName, 'a') as f:
        f.write(text)
def read(FileName):
    try:
        f=open(FileName, 'r')
        text=f.read()
        print(text)
        f.close()
    except FileNotFoundError:
        print("File doesn't exist")
        
def search(FileName, word):
    try:
        f=open(FileName, 'r')
        line_count=0
        for line in f.readlines():
            line_count+=1
            strlist =line.split(' ')
            word_count=0
            for w in strlist:
                word_count+=1
                if word ==w:
                    return(line_count, word_count)


        else:
            return None
            f.close()
    except FileNotFoundError:
        print("File Not Found")
            
        
