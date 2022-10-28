#! python 3
'''
selectiveCopy.py

    searches for file extensions in a root folder
    and copies them to a new folder

    Arguments:
    source destination extension
    
'''

import sys, os

args = sys.argv
argsl = len(args)

def askSrc():
    workDir = ''
    # if absolute directory & exists
    while not (os.path.isabs(workDir) and os.path.exists(workDir)):
        workDir = input('Source: ')
    return workDir

def askDst():
    workDir = ''
    # if absolute path & doesn't exist
    # not ( True and (not False) ) == break
    while not (os.path.isabs(workDir) and (not os.path.exists(workDir))):
        workDir = input('Destination: ')
    return workDir

def askExtension():
    return input('Extension: ')

def copy():
    # Handle first argument
    if not (argsl >= 2 and arsgl <= 4):
        src = askSrc()
    else:
        src = args[2]
    # Handle second argument   
    if not (argsl >= 3 and arsgl <= 4):
        dst = askDst()
    else:
        dst = args[3]
    # Handle third argument    
    if not (argsl == 4):
        ext = askExtension()
    else:
        ext = args[4]

    txt = '1:{}\n2:{}\n3:{}'
    print(txt.format(src, dst, ext))

copy()
