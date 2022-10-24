import random, sys

player = 0
computer = 0
tie = 0

def RPS():
    print('\nType exit to exit\n')
    print('\nWin: ' + str(player) + '\n' +
          'Lose: ' + str(computer) + '\n' +
          'Tie: ' + str(tie) + '\n')
    print('Rock(r), Paper(p), Scissors(s), shoot!: ', end='')

    bot = random.choice(['Rock', 'Paper', 'Scissors'])
    bP = str(bot[0]).lower() #first letter lowercase

    #print('DEBUG: Bot uses ' + bP)
    
    user = input()
    try:
        
        uP = str(user[0]).lower()
    
        
        if(user == 'exit'):
            sys.exit()
        
        print('=========== ' + user + ' vs ' + bot + ' ===========')
     

        if(uP == 'r' or uP == 'p' or uP == 's'):
            results = uP + bP
            switchResults(results, uP)

            RPS()
        else:
            print('Invalid Choice, Try again...\n')
            RPS()
            
    except IndexError:
        print('Empty, try again...')
        RPS()

def switchResults(result, uP):
    global player, computer, tie
    if(result == 'rr' or result == 'pp' or result == 'ss'):
        print('Tie')
        tie = tie + 1
    elif( (result == 'rs' and uP == 'r') or
          (result == 'pr' and uP == 'p') or
          (result == 'sp' and uP == 's') ):
        print('Player wins')
        player = player + 1
    else:
        print('Computer wins')
        computer = computer + 1
    
RPS()
