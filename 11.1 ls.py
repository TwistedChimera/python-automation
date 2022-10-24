import os, pprint
os.chdir('C:\\Users\\sulla\\Downloads\\Automate the Boring Stuff with Python Programming\\[TutsNode.com] - Automate the Boring Stuff with Python Programming')
for currentfolder, subfolders, files in os.walk(os.getcwd()):
    print()
    print('DEBUG: currentfolder')
    print(currentfolder)
    if not len(subfolders) == 0:
        print('DEBUG: subfolders')
        print(' -d- ', end='')
        print('\n -d- '.join(subfolders))
    if not len(files) == 0:
        print('DEBUG: files')
        print(' --f-- ', end='')
        print('\n --f-- '.join(files))
