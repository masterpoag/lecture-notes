Looking_for= ["spanish-american","treaty of paris","philippines","filipinos","Filipino war","imperialism"]

import os,re

countDict = {}
for key in Looking_for:
    countDict[key] = 0

try:
    os.remove("finished.txt")
except:
    print("already deleated")


f = open("finished.txt","a")

FOLDER_LOC = "notes/"
FOLDER_CONTENT = os.listdir(FOLDER_LOC)
for i in FOLDER_CONTENT:
    index = FOLDER_CONTENT.index(i)
    FOLDER_CONTENT[index] = FOLDER_LOC+i

def counter(s,t):
    counter = 0
    for i in s:
        if i == t:
            counter +=1
    return counter

count = 0
total = 0

def txtWriter(line,f):
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

for note in FOLDER_CONTENT:
    with open(note) as file:
        txtWriter(file.read(),f)
print("Found:",total)
print(countDict)