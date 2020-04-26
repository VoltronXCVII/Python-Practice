import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # The added parentheses are called 'groups'. 
mo = phoneNumRegex.search('My phone number is 775-223-1145')
print('The area code is ' + mo.group(1)) # Can pass a group number to the .group() function to display only that group.
# If wanting to have parentheses in the group, use the escape character "\"

# Can search text that has similar patterns in various scenarios using the pipe character "|".
# See example below. Will search for 'Batman', 'Batmobile', 'Batcopter' and 'Batbat'.
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel.')
print(mo.group())

# Can still call a specific group number in the .group() function.

print(mo.group(1))

# If nothing found in text, will return a 'None' value and will get an error when trying to call .group()