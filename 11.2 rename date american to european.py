import shutil, re, os

# regex for american dates
# NOTE: can't differentiate us & eur
#       when DD & MM are both <= 12
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
  [-]) # include separator (-)
  
  
  
  (?P<DD>
    [0123]?\d
  [-]) # include separator (-)
  
  
  
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
    os.chdir(rootDir)
    for root, dirs, files in os.walk(rootDir):
        for name in files:
            date = re.findall(usdateRegex, name)
            newname = name
            # change US to EUR date
            if len(date) > 0:
                # Dry run
                '''
                print('found us date:  ' + name)
                newname = str(swaptext(name, date[0][1], date[0][3]))
                print('us to eur date: ' + newname)
                print()
                '''
                # TODO: rename files
                shutil.move(name,newname)

# doesn't swap unless a and b are consecutive                
def swaptext(text, a, b):
    
    ## global swap which can overmatch ##
    
    # stack overflow solution:
    #return b.join(part.replace(b, a) for part in text.split(a))
    
    ''' ----------------------- '''
    
    ## single swap implementation ##
    
    aindex = text.index(a)
    alen = aindex + len(a)
    bindex = text.index(b)
    blen = bindex + len(b)
    # if a > b, swap values to prevent IndexError
    # and if they're next to each other (not necessary though)
    if((aindex > bindex) and (aindex - bindex == len(b))):
        aindex, bindex = bindex, aindex
        alen, blen = blen, alen
        a, b = b, a
    # swap a and b and only if they're next to each other
    if((bindex > aindex) and (bindex - aindex == len(a))):
        return text[:aindex] + text[bindex:blen] + text[aindex:alen] + text[blen:]
    else:
        print('ERR: swaptext')



workDir = DEBUG_askDirectory()
scanTree(workDir)
