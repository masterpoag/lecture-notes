Looking_for= []

import os,re
importance = 10
def update_search():
    global Looking_for
    while True:
        user = input("What you want want to search for one at a time? (enter -1 to end)\n").strip()
        if user == "-1":
            break
        Looking_for.append(user)

def removeSearch():
    global Looking_for
    loop = True
    while loop:
        os.system('cls||clear')
        print("-1) clear all\n0) close menu")
        for i in range(0,len(Looking_for)):
            print(f"{i+1}) {Looking_for[i]}")
        user = input("")
        
        try:
            if int(user.strip(),10) <= len(Looking_for):
                if int(user.strip(),10) == 0:
                    return
                if int(user.strip(),10) == -1:
                    Looking_for= []
                    return
                Looking_for.pop(int(user.strip(),10)-1)
            else:
                print("make sure to pick a option. (press enter to close)")
                input("")
                
        except:
            print("make sure to type a number. (press enter to close)")
            input("")


def initialization():
    global count, total
    try:
        FOLDER_LOC = open("config.cfg").read()
    except:
        f = open("config.cfg", "w")
        f.write("notes/")
    count = 0
    total = 0
    countDict = {}
    for key in Looking_for:
        countDict[key] = 0
    try:
        os.remove("finished.txt")
    except:
        print("already deleated")
    f = open("finished.txt","a")
    FOLDER_CONTENT = os.listdir(FOLDER_LOC)
    for i in FOLDER_CONTENT:
        index = FOLDER_CONTENT.index(i)
        FOLDER_CONTENT[index] = FOLDER_LOC+i
    search(FOLDER_CONTENT,countDict,f)

def counter(s,t):
    counter = 0
    for i in s:
        if i == t:
            counter +=1
    return counter

def ChangeFolder():
    f = open("config.cfg","w")
    f.write("Folder_LOC =",input("Where is the folder located? default: notes/\n").strip())



def txtWriter(line,countDict,note,f):
    global count,Looking_for,total,importance
    pattern = r'\b\d+:\d+\b'
    important = 0
    fixedWriting = re.sub(pattern,'',line).replace("\n","")
    fixedLine = fixedWriting.replace("U.S.","United States").replace(".",".\n").replace("?","?\n")
    for i in fixedLine.split("\n"):
        for n in Looking_for:
            if n.lower() in i.lower():
                countDict[n] += 1
                important = importance
                continue
        if counter(i," ") >= 3:
            if important != 0:
                if count == 0:
                    f.write(f"-----------------------------------------------------{note.split("/")[1]}-----------------------------------------------------\n")
                f.write(i.replace(".",".\n").replace("?","?\n"))
                count += 1
                if important != 0:
                    important -= 1
    total += count
    count = 0

def search(FOLDER_CONTENT,dict,f):
    for note in FOLDER_CONTENT:
        with open(note) as file:
            txtWriter(file.read(),dict,note,f)

def fileTest(FOLDER_CONTENT):
    print(FOLDER_CONTENT)

def set_importance():
    global importance
    try:
        user = input("pick a number as importance factor. (number of lines added on top of the line with the keywords) default: 10\n")
        importance = int(user.strip(),10)
    except:
        print("make sure to pick a option. (press enter to close)")
        input("")
        set_importance()


#TODO Add user interface
def UI():
    os.system('cls||clear')
    print(
"""Welcome to the Note Searcher. Ctrl+C to close
0) run search
1) set search
2) remove search
3) set notes location
4) set importance factor""")
    try:
        s = int(input("").strip(),10)
    except:
        print("make sure to type a number. (press enter to close)")
        input("")
        UI()
    os.system('cls||clear')
    match s:
        case 0:
            initialization()
            UI()
        case 1:
            update_search()
            UI()
        case 2:
            removeSearch()
            UI()
        case 3:
            ChangeFolder()
            UI()
        case 4:
            set_importance()
            UI()
        case _:
            print("make sure to pick a option. (press enter to close)")
            input("")
            UI()
UI()
