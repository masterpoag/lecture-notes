Looking_for= ["test","test12"]

import os,re

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
            if int(user.strip(),10) <= len(Looking_for) and not 0 and not -1:
                Looking_for.pop(int(user.strip(),10)-1)
            elif int(user.strip(),10) == 0:
                return
            elif int(user.strip(),10) == -1:
                Looking_for= []
            else:
                print("make sure to pick a option. (press enter to close)")
                input("")
            
        except:
            print("make sure to type a number. (press enter to close)")
            input("")


def initialization():
    global count, total
    with open("config.cfg") as file:
        FOLDER_LOC = file.read()
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
    search(FOLDER_CONTENT,countDict)

def counter(s,t):
    counter = 0
    for i in s:
        if i == t:
            counter +=1
    return counter

def ChangeFolder():
    f = open("config.cfg","w")
    f.write("Folder_LOC =",input("Where is the folder located?\n").strip())



def txtWriter(line,countDict,note,f):
    global count,Looking_for,total
    pattern = r'\b\d+:\d+\b'
    important = 0
    fixedWriting = re.sub(pattern,'',line).replace("\n","")
    fixedLine = fixedWriting.replace("U.S.","United States").replace(".",".\n").replace("?","?\n")
    
    for i in fixedLine.split("\n"):
        for n in Looking_for:
            if n.lower() in i.lower():
                countDict[n] += 1
                important = 10
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

def search(FOLDER_CONTENT,dict):
    for note in FOLDER_CONTENT:
        with open(note) as file:
            txtWriter(file.read(),dict,file)

removeSearch()
#TODO Add user interface
