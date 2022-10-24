import shutil, re

# TODO: regex for american dates
usdateRegex = re.compile(r'''
''', re.VERBOSE)

# TODO: ask which directory to work in
def askDirectory():
    workDir = input()

# TODO: scan whole directory
