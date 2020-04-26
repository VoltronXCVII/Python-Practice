import random, sys

theBoard = {'upper-L': ' ',
            'upper-M': ' ',
            'upper-R': ' ',
            'middle-L': ' ',
            'middle-M': ' ',
            'middle-R': ' ',
            'lower-L': ' ',
            'lower-M': ' ',
            'lower-R': ' '}

computerSpot = {1: 'upper-L',
                2: 'upper-M',
                3: 'upper-R',
                4: 'middle-L',
                5: 'middle-M',
                6: 'middle-R',
                7: 'lower-L',
                8: 'lower-M',
                9: 'lower-R'}

def showBoard(board):
    print(board['upper-L'] + '|' + board['upper-M'] + '|' + board['upper-R'])
    print('-----')
    print(board['middle-L'] + '|' + board['middle-M'] + '|' + board['middle-R'])
    print('-----')
    print(board['lower-L'] + '|' + board['lower-M'] + '|' + board['lower-R'])

def clearBoard():
    theBoard['upper-L'] = ' '
    theBoard['upper-M'] = ' '
    theBoard['upper-R'] = ' '
    theBoard['middle-L'] = ' '
    theBoard['middle-M'] = ' '
    theBoard['middle-R'] = ' '
    theBoard['lower-L'] = ' '
    theBoard['lower-M'] = ' '
    theBoard['lower-R'] = ' '

def playersTurn():
    print('Where would you like to go? (Rows: upper-, middle-, lower-  Columns: L, M, R)')
    userMove = input()
    if theBoard[userMove] == ' ':
        theBoard[userMove] = 'X' 
    elif theBoard[userMove] != ' ':
        print('That space is already taken')
        playersTurn()

def computersTurn():
    '''if ((theBoard[computerSpot[1]] != ' ') and
        (theBoard[computerSpot[2]] != ' ') and
        (theBoard[computerSpot[3]] != ' ') and
        (theBoard[computerSpot[4]] != ' ') and
        (theBoard[computerSpot[5]] != ' ') and
        (theBoard[computerSpot[6]] != ' ') and
        (theBoard[computerSpot[7]] != ' ') and
        (theBoard[computerSpot[8]] != ' ') and
        (theBoard[computerSpot[9]] != ' ')
    ):
        print('It\'s a tie!')
    if:'''
    randNum = random.randint(1,9)
    if theBoard[computerSpot[randNum]] == ' ':
        theBoard[computerSpot[randNum]] = 'O'
    elif theBoard[computerSpot[randNum]] != ' ':
        computersTurn()
    


def gameProcess():
    while gameStatus.lower() == 'yes':
        if ((theBoard[computerSpot[1]] =='O' and theBoard[computerSpot[2]] =='O' and theBoard[computerSpot[3]] =='O')
            or (theBoard[computerSpot[4]] =='O' and theBoard[computerSpot[5]] =='O' and theBoard[computerSpot[6]] =='O')
            or (theBoard[computerSpot[7]] =='O' and theBoard[computerSpot[8]] =='O' and theBoard[computerSpot[9]] =='O')
            or (theBoard[computerSpot[1]] =='O' and theBoard[computerSpot[4]] =='O' and theBoard[computerSpot[7]] =='O')
            or (theBoard[computerSpot[2]] =='O' and theBoard[computerSpot[5]] =='O' and theBoard[computerSpot[8]] =='O')
            or (theBoard[computerSpot[3]] =='O' and theBoard[computerSpot[6]] =='O' and theBoard[computerSpot[9]] =='O')
            or (theBoard[computerSpot[1]] =='O' and theBoard[computerSpot[5]] =='O' and theBoard[computerSpot[9]] =='O')
            or (theBoard[computerSpot[3]] =='O' and theBoard[computerSpot[5]] =='O' and theBoard[computerSpot[7]] =='O')
        ):  
            showBoard(theBoard)
            print('The Computer won!')
            break

        elif ((theBoard[computerSpot[1]] =='X' and theBoard[computerSpot[2]] =='X' and theBoard[computerSpot[3]] =='X')
            or (theBoard[computerSpot[4]] =='X' and theBoard[computerSpot[5]] =='X' and theBoard[computerSpot[6]] =='X')
            or (theBoard[computerSpot[7]] =='X' and theBoard[computerSpot[8]] =='X' and theBoard[computerSpot[9]] =='X')
            or (theBoard[computerSpot[1]] =='X' and theBoard[computerSpot[4]] =='X' and theBoard[computerSpot[7]] =='X')
            or (theBoard[computerSpot[2]] =='X' and theBoard[computerSpot[5]] =='X' and theBoard[computerSpot[8]] =='X')
            or (theBoard[computerSpot[3]] =='X' and theBoard[computerSpot[6]] =='X' and theBoard[computerSpot[9]] =='X')
            or (theBoard[computerSpot[1]] =='X' and theBoard[computerSpot[5]] =='X' and theBoard[computerSpot[9]] =='X')
            or (theBoard[computerSpot[3]] =='X' and theBoard[computerSpot[5]] =='X' and theBoard[computerSpot[7]] =='X')
        ):
            showBoard(theBoard)
            print('You won!')
            break 

        

        else:
            showBoard(theBoard)
            playersTurn()
            if ((theBoard[computerSpot[1]] != ' ') and
                (theBoard[computerSpot[2]] != ' ') and
                (theBoard[computerSpot[3]] != ' ') and
                (theBoard[computerSpot[4]] != ' ') and
                (theBoard[computerSpot[5]] != ' ') and
                (theBoard[computerSpot[6]] != ' ') and
                (theBoard[computerSpot[7]] != ' ') and
                (theBoard[computerSpot[8]] != ' ') and
                (theBoard[computerSpot[9]] != ' ')
            ):
                print('It\'s a tie!')
                break
            else:
                computersTurn()

        

def playGame(status):
    if status.lower() == 'yes':
        print('Ok! You\'re X!')
        gameProcess()
    elif status.lower() == 'no':
        print('Ok. Goobye.')
        sys.exit()
    else:
        print('Didn\'t recognize your input.')
        gameStatus = input()
        playGame(gameStatus)

def playAgain(status):
    if status.lower() == 'yes':
        clearBoard()
        print('Ok! You\'re X!')
        gameProcess()
    elif status.lower() == 'no':
        print('Ok. Goobye.')
        sys.exit()
    else:
        print('Didn\'t recognize your input.')
        gameStatus = input()
        playAgain(gameStatus)

print('Would you like to play a game of Tic Tac Toe?')
gameStatus = input()
playGame(gameStatus)

#print('Would you like to play again?')
#gameStatus = input()
#playAgain(gameStatus)