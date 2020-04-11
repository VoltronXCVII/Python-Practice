import random

# Test for using Git on raspberry pi

def randomNum():
    randNum = random.randint(1,100)
    return randNum

def guessNum():
    rand = randomNum()
    print('I\'m thinking of a number between 1 and 100. Try to guess what it is.')
    guess = int(input())
    myLoop = False
    attempts = 1
    while myLoop == False:
        if guess == rand:
            myLoop = True
            print('You guessed it! I was thinking of ' + str(rand) + '! It took you ' + str(attempts) + ' tries.')
            if attempts < 5:
                print('You\'re pretty good at this!')
            else:
                print('Wow. ' + str(attempts) + ' tries. Not your best.')
            playAgain()
        elif guess > rand:
            attempts += 1
            print('Too high, the number I\'m thinking of is lower than ' + str(guess) + '. Guess again.')
            guess = int(input())
        elif guess < rand:
            attempts += 1
            print('Too low, the number I\'m thinking of is higher than ' + str(guess) + '. Guess again.')
            guess = int(input())
            
def playAgain():            
    print('Would you like to play again? (Yes/No)')
    play = input()
    if play == 'Yes' or play == 'yes':
        guessNum()
    elif play == 'No' or play == 'no':
        print('Ok. See ya.')
    else:
        print('I didn\'t understand what you said. Please enter "Yes" or "No".')
        playAgain()

print('Hello. Would you like to play a game? (Yes/No)')
resp = input()
if resp == 'Yes' or resp == 'yes':
    guessNum()
elif resp == 'No' or resp == 'no':
    print('Ok. Have a nice day.')
else:
    print('I don\'t know what you mean by that. Please enter "Yes" or "No".')
