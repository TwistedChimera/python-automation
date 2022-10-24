import re

def strongPass(pw):
    passwordRegex= re.compile(r'''
    (?=[-_\=+!@#$%^&*()\[\]{}|\\;:'",.\/<>?a-zA-Z ]*[\d])  # need digit
    (?=[-_\=+!@#$%^&*()\[\]{}|\\;:'",.\/<>?\dA-Z ]*[a-z])  # need lower 
    (?=[-_\=+!@#$%^&*()\[\]{}|\\;:'",.\/<>?\da-z ]*[A-Z])  # need upper
    (?:[a-zA-Z-_\=+!@#$%^&*()\[\]{}|\\;:'",.\/<>?\d ]){8,} # min: 8 characters
    ''', re.VERBOSE)
    return True if ''.join(re.findall(passwordRegex, password)) == pw else False

while True:
    print('password: ', end='')
    password = input()
    if strongPass(password):
        print('strong password')
        break
    else:
        print('weak password')
