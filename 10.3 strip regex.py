import re
stripRegex = re.compile(r'[^ ].*[^ ]', re.DOTALL)
lstripRegex = re.compile(r'[^ ].*', re.DOTALL)
rstripRegex = re.compile(r'.*[^ ]', re.DOTALL)

spam = '''        text          '''

def strip(text, *args):
    if len(args) == 0:
        print('\'' + ''.join(re.findall(stripRegex, text)) + '\'')
    elif args[0] == 'lstrip':
        print('\'' + ''.join(re.findall(lstripRegex, text)) + '\'')
    elif args[0] == 'rstrip':
        print('\'' + ''.join(re.findall(rstripRegex, text)) + '\'')
    else:
        print('options: lstrip, rstrip')

strip(spam)
strip(spam, 'lstrip')
strip(spam, 'rstrip')
strip(spam, 'asdfasdf')
