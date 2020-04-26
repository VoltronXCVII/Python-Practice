# The below commented-out code is an example of a way to code a regualr expression to find a phone number in text.
# However, below that, is the same but using the built in Reg Ex modules in Python.
'''
def isPhoneNumber(text):
    if len(text) != 12:
        return False # Not phone number sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # No area code
    if text[3] != '-':
            return False # Missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # No first 3 digits
    if text[7] != '-':
        return False # Missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # Missing last 4 digits
    return True

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found.')
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')
'''

import re # This is the Regular Expression module

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # re.compile() is usually passed a raw string. The string passed is the pattern we want to find.
mo = phoneNumRegex.search(message) # .search() is passed the argument of what text you would like to search the pattern for. Returns a 'match object'.
print(mo.group())

# Can use .findall() to print out all occurences of the pattern in the text instead of .search() which gives only one occurence.

print(phoneNumRegex.findall(message)) # Returns a list.