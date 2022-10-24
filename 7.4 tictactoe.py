import random

# board
board = { 'a3': ' ', 'b3': ' ', 'c3': ' ',
          'a2': ' ', 'b2': ' ', 'c2': ' ',
          'a1': ' ', 'b1': ' ', 'c1': ' '}
# piece
o = 'o'
x = 'x'
# who holds which piece
player = ''
computer = ''
# turn
turnPlayer = '1'
turnComputer = '2'
turn = ''
turnToggle = ''
# difficulty
diffNormal = '1'
diffEasy = '2'
diffHard = '3'
difficulty = ''
# score
scorePlayer = '0'
scoreComputer = '0'
scoreTie = '0'
# empty positions
emptyPositions = []


def checkWin(piece):
    global board, player
    if (
        #Horizontal
        board['a3'] == board['b3'] == board['c3'] == piece or
        board['a2'] == board['b2'] == board['c2'] == piece or
        board['a1'] == board['b1'] == board['c1'] == piece or
        #Vertical
        board['a3'] == board['a2'] == board['a1'] == piece or
        board['b3'] == board['b2'] == board['b1'] == piece or
        board['c3'] == board['c2'] == board['c1'] == piece or
        #Diagonal
        board['a3'] == board['b2'] == board['c1'] == piece or
        board['a1'] == board['b2'] == board['c3'] == piece
        ):
        return True

def printWinner(piece):
    global player
    if (player == piece):
        print('Player wins!')
    else:
        print('Computer wins!')

def settings():
    global player, computer, o, x
    global turn, turnToggle, turnPlayer, turnComputer
    global difficulty, diffNormal, diffEasy, diffHard

    # Choose piece
    print('choose "' + o + '" or "' + x + '"')
    while not(player == o or player == x):
        player = input()
    if (player == o):
        computer = x
    else:
        computer = o

    # Choose turn order
    print('Turn order: Player(1) or Computer(2)')
    while not (turn == turnPlayer or turn == turnComputer):
        turn = input()
    turnToggle = int(turnPlayer) + int(turnComputer)
    turnToggle = str(turnToggle)

    # Choose difficulty
    print('Normal(1), Random(2), or Impossible (3)')
    while not (difficulty in [diffNormal, diffEasy, diffHard]):
        difficulty = input()
        
def printSettings():
    print('player: ' + player +'\ncomputer: ' + computer)
    if (difficulty == diffNormal):
        print('Difficulty: Normal')
    elif (difficulty == diffEasy):
        print('Difficulty: Easy')
    else:
        print('Difficulty: Impossible')
    if (turn == turnPlayer):
        print('turn order: Player -> Computer')
        printBoard()
    else:
        print('turn order: Computer -> Player')

def resetSettings():
    global player, computer, turn, difficulty
    global scorePlayer, scoreComputer, scoreTie
    player = ''
    computer = ''
    turn = ''
    difficulty = ''
    scorePlayer = '0'
    scoreComputer = '0'
    scoreTie = '0'

def clearBoard():
    global board
    board = { 'a3': ' ', 'b3': ' ', 'c3': ' ',
          'a2': ' ', 'b2': ' ', 'c2': ' ',
          'a1': ' ', 'b1': ' ', 'c1': ' '}

def printBoard():
    global board
    print(board['a3'] + '|' + board['b3'] + '|' + board['c3'] + ' 3')
    print('-+-+-')
    print(board['a2'] + '|' + board['b2'] + '|' + board['c2'] + ' 2')
    print('-+-+-')
    print(board['a1'] + '|' + board['b1'] + '|' + board['c1'] + ' 1')
    print('a b c')

def scoreBoard():
    global scorePlayer, scoreComputer, scoreTie
    print('=========== score ===========')
    print('Player: ' + scorePlayer)
    print('Computer: ' + scoreComputer)
    print('Tie: ' + scoreTie)
    print('=============================')

def scoreIncrement(piece):
    global player, computer, scorePlayer, scoreComputer, scoreTie
    if (player == piece):
        scorePlayer = int(scorePlayer) + 1
        scorePlayer = str(scorePlayer)
    elif (computer == piece):
        scoreComputer = int(scoreComputer) + 1
        scoreComputer = str(scoreComputer)
    else:
        scoreTie = int(scoreTie) + 1
        scoreTie = str(scoreTie)

def move(position, piece):
    global turn, turnToggle
    # only move on correct turn
    if ((turn == turnPlayer and piece == player) or
        (turn == turnComputer and piece == computer)):
        if position in board.keys(): # if position (key) exists
            if board[position].isalpha(): # if position is taken
                illegal()
                moveAgain()
            else:
                # place piece
                board[position] = piece
                # show board
                printBoard()
                # toggle turn
                turn = int(turnToggle) - int(turn) # 1 = 3 - 2 or 2 = 3 - 1
                turn = str(turn) 
        else:
            illegal()
            moveAgain()

def replace(position, piece):
    global board
    board[position] = piece

def illegal():
    print('illegal move')
    
def moveAgain():
    global player
    position = input()
    move(position, player)
    
def movePlayer(position):
    global turn, turnPlayer, player
    if (turn == turnPlayer):
        move(position, player)

def printMove(position, piece):
    global player
    if (player == piece):
        print('player moved piece to: ' + position)
    else:
        print('computer moved piece to: ' + position)

def moveAiRandom():
    global computer, turn, turnComputer, emptyPositions
    if (turn == turnComputer):
        position = random.choice(emptyPositions) # Choose random key
        printMove(position, computer)
        move(position, computer)

def simulateWin():
    global computer, player, turn, turnComputer, emptyPositions
    # simulate legal moves and see if winning
    
    if (turn == turnComputer and len(emptyPositions) > 0):
        for position in emptyPositions:
            replace(position, computer)
            if (checkWin(computer)):
                print('Computer found winning move ' + str(position))
                replace(position, ' ')
                move(position, computer) # move only works on empty positions
                break
            # reset position
            replace(position, ' ')

    # simulate player moves and block if winning
    if (turn == turnComputer and len(emptyPositions) > 0):
        for position in emptyPositions:
            replace(position, player)
            if (checkWin(player)):
                print('Computer blocks with ' + str(position))
                replace(position, ' ')
                move(position, computer)
                break
            # reset position
            replace(position, ' ')

def randCorner():
    global computer, turn, turnComputer, emptyPositions
    if (turn == turnComputer and len(emptyPositions) > 0):
        pickRandom(['a3','a1','c3','c1'], computer)
        
def randSide():
    global computer, turn, turnComputer, emptyPositions
    if (turn == turnComputer and len(emptyPositions) > 0):
        pickRandom(['a2','b3','c2','b1'], computer)
        
def center():
    global computer, turn, turnComputer, emptyPositions
    if (turn == turnComputer and len(emptyPositions) > 0):          
        center = 'b2'
        if center in emptyPositions:
            printMove(center, computer)
            move(center, computer)

def pickRandom(positionList, piece):
    global turn, turnComputer, emptyPositions
    legalPositions = []
    for position in positionList:
        if (position in emptyPositions):
            legalPositions.append(position)
    position = random.choice(positionList)
    printMove(position, piece)
    move(position, piece)

def scanEmptyPositions():
    global board
    emptyPositions = []
    for key, value in board.items(): # Scan all tuples
        if (value == ' '): # Grab tuple value, see if empty
            emptyPositions.append(key) # if empty, grab key
    return emptyPositions
            
def moveAi():
    global computer, player, turn, turnComputer

    # simulate legal moves and see if winning
    # simulate player moves and block if winning
    simulateWin()

    # pick a random corner if available        
    randCorner()

    # pick center if available    
    center()

    # pick random side if available        
    randSide()
    
def moveAiHard():
    global board, computer, player, turn, turnComputer

    # simulate legal moves and see if winning
    # simulate player moves and block if winning
    simulateWin()
    
    # avoid center if first
    if(x in list(board.values()) or o in list(board.values())):
        # pick center if available    
        center()
        
    # pick a random corner if available        
    randCorner()
    
    # pick random side if available        
    randSide()

def loopGame():
    print('Change settings? (y/[n])')
    
    changeSettings = input()
    if (len(changeSettings) > 0):
        if(changeSettings[0].lower() == 'y'):
            resetSettings()
            settings()
            printSettings()
            startGame()
    printSettings()
    startGame()

def startGame():
    global turn, player, computer
    global difficulty, diffNormal, diffEasy, diffHard
    while ' ' in board.values(): # if there's empty space, continue
        # Player
        if (turn == turnPlayer):
            position = input()
            movePlayer(position)
        if (checkWin(player)):
            printWinner(player)
            scoreIncrement(player)
            break
        # Computer
        if difficulty == diffNormal:
            moveAi()
        elif difficulty == diffEasy:               
            moveAiRandom()
        elif difficulty == diffHard:
            moveAiHard()
        # Check winner
        if (checkWin(computer)):
            printWinner(computer)
            scoreIncrement(computer)
            break
    # if no winner
    if (checkWin(player) == None and checkWin(computer) == None):
        print('Tie')
        scoreIncrement('Tie')
    clearBoard()
    scoreBoard()
    loopGame()

settings()
printSettings()
startGame()

    
