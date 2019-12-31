import random

# Load a list of first names 
first = ("PurtyPrincess", "PinHeadLarry", "DeathDealer", "DirtyDan", "DrFreeBase", "Gengar", "BringATowel", "BoKnows")

# Load a list of last names
last = ("The Goat", "Trash Panda", "The Camper", "The Gay", "The Hard Charger")
c = '1'
while c == '1':
# Choose a first name at random
# Assign the name to a variable
    rand_first = random.choice(first)

# Choose a surname at random
# Assign the name to a variable
    rand_last = random.choice(last)

# Print the names to the console in order and in red font
    print('\033[91m %s %s\033[0m' % (rand_first, rand_last))

# Ask the user to quit or play again
    
# If user plays again: 
#   repeat
    c = input("Do you wish to play again? \n Enter 1 for yes, or press enter to exit.")