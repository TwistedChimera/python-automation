import shutil, re, os

# TODO: regex for american dates
usdateRegex = re.compile(r'''
(?P<DATE>
  (?P<MM>
    # check first digit if 0 or 1
    (?P<M>[01])?
    # ternary operator, If previous is 0 or 1 ? True : False
    (?(M)
        # if True, second digit can only be 0,1,2
        [012]
        # if False, second digit can't be 2 or 3
        |(?<![123])\d
    )
  )
  
  [-]
  
  (?P<DD>
    [0123]?\d
  )
  
  [-]
  
  (?P<YYYY>
    [12]\d\d\d
  )
)
''', re.VERBOSE)
'''
[0] DATE
[1] MM
[2] M
[3] DD
[4] YYYY
'''

# ask which directory to work in
def askDirectory():
    workDir = input()
    while not os.path.exists(workDir):
        workDir = input()
    return workDir

# DEBUG: remove function after testing
def DEBUG_askDirectory():
    workDir = r'''C:\Users\sulla\Downloads\Automate the Boring Stuff with Python Programming\[TutsNode.com] - Automate the Boring Stuff with Python Programming\11. Files\generated'''
    while not os.path.exists(workDir):
        workDir = input()
    return workDir

# TODO: scan whole directory
def scanTree(rootDir):
    for root, dirs, files in os.walk(rootDir):
        for name in files:
            date = re.findall(usdateRegex, name)
            newname = name
            # change US to EUR date
            if len(date) > 0:
                print('found us date:  ' + name)
                newname = swaptext(name, date[0][1], date[0][3])
                print('us to eur date: ' + newname)
                print()
                
def swaptext(text, a, b):
    return b.join(part.replace(b, a) for part in text.split(a))


workDir = DEBUG_askDirectory()
scanTree(workDir)
