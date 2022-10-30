#! python3
'''
findLargeFiles

    find large files >100MB in a selected folder

'''
import os, sys

args = sys.argv
argsl = len(args) - 1

def getSrc():
    global args
    # initialize
    src = ''
    # if source is supplied as argument
    if (argsl == 1):
        src = args[1]
    # if absolute path & is a directory
    while not (os.path.isabs(src) and os.path.isdir(src)):
        src = input('Source: ')
    return src

def search():
    src = getSrc()

    txt = '{} {:.2f}MB'
    for pwd, folders, files in os.walk(src):
        for name in files:
            filePath = os.path.join(pwd, name)
            fileSize = os.path.getsize(filePath)/(1024*1024)
            if(fileSize >= 100):
                print(txt.format(filePath,fileSize))
    
search()
