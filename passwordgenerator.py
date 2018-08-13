# Author: Colin Gillette
# Purpose: Generate a 7 character password that meets specific requirements

import string
import random

# Starting arrays for random indicies to choose from
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = list(range(0, 10))
specialchar = '!#$@?'

# Random seeds to choose from arrays
letterseed1 = random.randrange(0, 25)
letterseed2 = random.randrange(0, 25)
letterseed3 = random.randrange(0, 25)
letterseed4 = random.randrange(0, 25)

numseed1 = random.randrange(0, 9)
numseed2 = random.randrange(0, 9)

specseed1 = random.randrange(0, 4)

# Assign random characters
lower1 = lower[letterseed1]
upper1 = upper[letterseed2]
lower2 = lower[letterseed3]
upper2 = upper[letterseed4]
num1 = numbers[numseed1]
num2 = numbers[numseed2]
spec1 = specialchar[specseed1]

# Create arrays of selected characters and give a shuffled index to randomly arrange characters
options = upper1 + upper2 + lower1 + lower2 + str(num1) + str(num2) + spec1
index = list(range(0, 7))
random.shuffle(index)

# Create the random password
pword = ''
for item in index:
    pword += str(options[item])
print(pword)

# Write the password to a text file
path = 'C:/A/Normal/path/pword.txt'
file = open(path, 'w')
file.write(pword)
file.close()