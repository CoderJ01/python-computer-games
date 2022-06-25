import random # provides randint(), which was used also for guessing game
import time 

def displayIntro(): # displatIntro is a function
    # Use multiline strings (three quotes) to enable string to go across several lines
    print(''' You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his teasure with you. The other dragon
is greedy and hundry, and will eat you on sight.''')
    print()

# Ask player to choose which cave to enter
def chooseCave():
    # local variable
    cave = ''
    # while loops loops if player choses any number other than 1 or 2 (aka 'input validation').
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave;

# chosenCave is a parameter
def checkCave(chosenCave):
    print('You appraoch the cave...')
    time.sleep(2) # time module pauses the code, the 2 sets the pause for two seconds
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)') # Remember that 'YES' != 'yes'
    playAgain = input()


#
# additional concepts
#

# Booleans
    # True and True evaluates to True
    # True and False evaluates to False
    # False and True evaluates to False
    # False and False evaluates to False

    # True or True evaluates to True
    # True or False evaluates to True
    # False or True evaluates to True
    # False or False evaluates to False

#len()
# Uncomment bottom code snippet, commet 'playAgain' code block to for code below to run
"""
len('Hello') # returns the characters in a string, in this case 5
print('Enter your name: ')
name = input()
def sayHello(name):
    print('Hello ' + name + ', your name has ' + str(len(name)) + ' letters.');
sayHello(name)
"""

