def encodeWord(usrWord):
    wordLen = len(usrWord)
    encription = ""
    n = 1

    while n <= wordLen:
        for i in usrWord.lower():
            if i == 'a':
                encription += '?'
            elif i == 'b':
                encription += '#'
            elif i == 'c':
                encription += ')'
            elif i == 'd':
                encription += '$'
            elif i == 'e':
                encription += '!'
            elif i == 'f':
                encription += '*'
            elif i == 'g':
                encription += '6'
            elif i == 'h':
                encription += '='
            elif i == 'i':
                encription += '+'
            elif i == 'j':
                encription += '-'
            elif i == 'k':
                encription += '@'
            elif i == 'l':
                encription += '~'
            elif i == 'm':
                encription += '`'
            elif i == 'n':
                encription += '<'
            elif i == 'o':
                encription += '4'
            elif i == 'p':
                encription += '3'
            elif i == 'q':
                encription += '|'
            elif i == 'r':
                encription += '{'
            elif i == 's':
                encription += '.'
            elif i == 't':
                encription += ','
            elif i == 'u':
                encription += ';'
            elif i == 'v':
                encription += '2'
            elif i == 'w':
                encription += '5'
            elif i == 'x':
                encription += '9'
            elif i == 'y':
                encription += '8'
            elif i == 'z':
                encription += '%'
            elif i ==' ':
                encription += '^'
            n += 1

        return encription

def decodeWord(usrCode):
    wordLen = len(usrCode)
    decription = ""
    n = 1

    while n <= wordLen:
        for i in usrCode:
            if i == '?':
                decription += 'a'
            elif i == '#':
                decription += 'b'
            elif i == ')':
                decription += 'c'
            elif i == '$':
                decription += 'd'
            elif i == '!':
                decription += 'e'
            elif i == '*':
                decription += 'f'
            elif i == '6':
                decription += 'g'
            elif i == '=':
                decription += 'h'
            elif i == '+':
                decription += 'i'
            elif i == '-':
                decription += 'j'
            elif i == '@':
                decription += 'k'
            elif i == '~':
                decription += 'l'
            elif i == '`':
                decription += 'm'
            elif i == '<':
                decription += 'n'
            elif i == '4':
                decription += 'o'
            elif i == '3':
                decription += 'p'
            elif i == '|':
                decription += 'q'
            elif i == '{':
                decription += 'r'
            elif i == '.':
                decription += 's'
            elif i == ',':
                decription += 't'
            elif i == ';':
                decription += 'u'
            elif i == '2':
                decription += 'v'
            elif i == '5':
                decription += 'w'
            elif i == '9':
                decription += 'x'
            elif i == '8':
                decription += 'y'
            elif i == '%':
                decription += 'z'
            elif i == '^':
                decription += ' '
            n += 1
        return decription

def encodeOrDecode():
    print('Enter \'Encode\' to produce a code for a word or \'Decode\' to decode a word.')
    userAns = input()
    userAns.lower()

    if userAns == 'encode':
        print('Input a word you would like encoded.')
        orgWord = input()
        codedWord = encodeWord(orgWord)
        print('Your encription for the word, ' + orgWord + ' is \" ' + codedWord + ' \"')
        goAgain()
    elif userAns == 'decode':
        print('Input a code you would like decoded.')
        orgCode = input()
        decodedWord = decodeWord(orgCode)
        print('The word from the code ' + orgCode + ' is \" ' + decodedWord + ' \"')
        goAgain()
    else:
        print('Didn\'t recognize your input.')
        encodeOrDecode()

def goAgain():
    print('Would you like to use the encoder again? (Y/N)')
    usrRetry = input()
    usrRetry.lower()

    if usrRetry == 'y':
        encodeOrDecode()
    elif usrRetry == 'n':
        print('Goodbye.')


encodeOrDecode()
