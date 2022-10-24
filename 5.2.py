print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) < 0:
        print('You have negative cats?')
    else:
        print('This is not that many cats.')
except ValueError:
    print('You did not enter a number.')
