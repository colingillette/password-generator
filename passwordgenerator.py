# Author: Colin Gillette
# Purpose: Generate a password that meets specific requirements

import string
import random

def rand_seed(items):
    items -= 1
    rand = random.randrange(0, items)
    return rand

def make_password():
    # Starting arrays for random indicies to choose from
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = list(range(0, 10))
    specialchar = '!#$@?'
    options = ''

    # Random seeds to choose from arrays
    letterseed1 = rand_seed(len(lower))
    letterseed2 = rand_seed(len(upper))
    letterseed3 = rand_seed(len(lower))
    letterseed4 = rand_seed(len(upper))

    numseed1 = rand_seed(len(numbers))
    numseed2 = rand_seed(len(numbers))

    specseed1 = rand_seed(len(specialchar))
    specseed2 = rand_seed(len(specialchar))

    # Assign random characters
    for x in range(9):
        if x % 2 == 0:
            if x % 4 == 0:
                seed = rand_seed(len(upper))
                options += str(upper[seed])
            else:
                seed = rand_seed(len(lower))
                options += str(lower[seed])
        else:
            if x == 3:
                seed = rand_seed(len(specialchar))
                options+= str(specialchar[seed])
            else:
                seed = rand_seed(len(numbers))
                options += str(numbers[seed])

    # Create arrays of selected characters and give a shuffled index to randomly arrange characters
    index = list(range(0, 7))
    random.shuffle(index)

    # Create the random password
    pword = ''
    for item in index:
        pword += str(options[item])
    return pword

# Main Body
times = int(input("Please enter the number of passwords you would like to make: "))
times

for password in range(times):
    print(make_password())

