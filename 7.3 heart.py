heart = '''..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....'''

dumpList = []
goodList = []

def listinator(itemList):
    global dumpList, goodList
    for index in range(len(itemList)):
        dumpList.append(itemList[index])  
        if (itemList[index] == '\n'):     
            goodList.append(dumpList[:-1])
            dumpList = [] 

listinator(heart)

for x in goodList:
    print(x)

