print('Input a word you would like encoded')
orgWord = input()

def encodeWord():
    wordLen = len(orgWord)
    encription = ""
    n = 1

    while n <= wordLen:
        for i in orgWord.lower():
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
                encription += '^'
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
            n += 1
        return encription

codedWord = encodeWord()
print('Your encription for the word, ' + orgWord + ' is \" ' + codedWord + ' \"')