#! python3
'''
BackupToZip.py

    Copies an entire folder and its contents into
    a ZIP file whose filename increments
    
'''


import os, zipfile

def askDir():
    workDir = ''
    while not os.path.isdir(workDir):
        print('Folder to backup: ', end='')
        workDir = input()
    return workDir

def backupToZip(workDir):
    
    parent = os.path.dirname(workDir)
    
    # break if absolute path and if parent exists
    while not (os.path.abspath(workDir) and os.path.exists(parent)):
        workDir = askDir()
        parent = os.path.dirname(workDir)

    # Create backup on parent folder
    os.chdir(parent)

    # Increment per existing backup
    counter = 1
    while True:
        zipName = os.path.basename(workDir) + '_' + str(counter) + '.zip'
        if not os.path.exists(zipName):
            break
        counter += 1
    
    # Create the ZIP file
    txt = 'Creating {}...'
    print(txt.format(zipName))
    bakZip = zipfile.ZipFile(zipName, 'w')

    # Relative path from workDir
    os.chdir(workDir)
    
    txt2 = 'file: {}'
    # Walk folder tree and copy to bakZip
    for pwd, folders, files in os.walk(workDir):
        # add each file in each folder    
        for name in files:
            print(txt2.format(os.path.join(pwd,name)))
            bakZip.write(os.path.relpath(os.path.join(pwd,name)))
    bakZip.close()
    print('Success.')

backupToZip(askDir())
