# Must import built in modules before using them
import random

# using a '.' after a module name tells computer to look in that module for the function being used.

print(random.randint(1,10))

# Import multiple modules at once
import random, sys, os, math

# Can import certain functions from a module, at this point, you can just call the function without having to restate the module followed by a '.'
from random import randint
print(randint(1,10))

# Can also import all functinos within the module by using a '*'. Be aware that this may make it harder to follow you code. 
from random import *


# sys.exit() allows will exit the program. Note when running this code the 'goodbye' doesn't print.
print('hello')
sys.exit()
print('goodbye')