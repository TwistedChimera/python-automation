#! python 3
'''
selectiveCopy.py

    searches for file extensions in a root folder
    and copies them to a new folder

    Arguments:
    source destination extension
    
'''

import sys, os, re, shutil

args = sys.argv
argsl = len(args) - 1 # don't include first element




def getSrc():
    global args
    # initialize
    src = ''
    # if source is supplied as argument
    if (argsl>=1 and argsl<=3):
        src = args[1]
    # if absolute path & is a directory
    while not (os.path.isabs(src) and os.path.isdir(src)):
        src = input('Source: ')
    return src

def getDst():
    global args
    # initialize 
    dst = ''
    # if destination is supplied as argument
    if (argsl>=2 and argsl<=3):
        dst = args[2]
    # if absolute path & doesn't exist & is a directory
    # not ( True and (not False) and True) == break
    while not (os.path.isabs(dst) and (not os.path.exists(dst))):
        dst = input('Destination: ')
    return dst

def getExt():
    global args
    # initialize
    ext = ''
    # if extension is supplied as argument
    if (argsl == 3):
        ext = args[3]
    # loop while ext is empty
    while(ext == ''):
        ext = input('Extension: ')
    return ext

def main():
    src = getSrc()
    dst = getDst()
    ext = getExt()

    pattern = r'''.*[.]''' + ext + '$'
    extRegex = re.compile(pattern)
    
    # move to source folder
    os.chdir(src)
    # uncomment 1/2 to actually copy
    #os.mkdir(dst)
    
    # walk source folder tree
    matches = []
    for pwd, folders, files in os.walk(src):
        for name in files:
            matchList = re.findall(extRegex, name)
            if len(matchList) == 1:
                matches.append(os.path.join(pwd,matchList[0]))
                # uncomment 2/2 to actually copy
                #shutil.copy(os.path.join(pwd,matchList[0]),dst)
                
    txt = 'matches: {}'
    for name in matches:
        print(txt.format(name))
            
            
    

main()
