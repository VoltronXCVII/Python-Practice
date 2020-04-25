import random

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


def playersTurn():
    showBoard(theBoard)
    print('Where would you like to go? (Rows: upper-, middle-, lower-  Columns: L, M, R)')
    userMove = input()

    if theBoard[userMove] == ' ':
        theBoard[userMove] = 'X' 
    elif theBoard[userMove] != ' ':
        print('That space is already taken')
        playersTurn()

def computersTurn():
    randNum = random.randint(1,9)

    if theBoard[computerSpot[randNum]] == ' ':
        theBoard[computerSpot[randNum]] = 'O'
    elif theBoard[compterSpot[randNum]] != ' ':
        computersTurn()
    showBoard(theBoard)


    

playGame = 'yes'
playGame.lower()

#while playGame == 'yes':
    #playersTurn()
computersTurn()
