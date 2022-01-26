#Damon Nutter
#006315383
# nim_2compl.py
# game of Nim, CSE 5120, Fall 2020
# Option for HW1: complete code where indicted with ADD

import random    # for random numbers

# create a game of nim with 3 piles of k stones
def nim_setup(k):
    mynim = [k,k,k]
    return mynim

# display the state of the nim game
def show_nim(nim):
    for i in range(3):
        print ("\npile %d: " % (i+1), end = ''),
        for i in range(nim[i]):
            print ("@", end = ''),
    print ("\n")

# the play function
# make a game, player and computer take turns
# making nim moves until all piles are empty
# and last player loses ...

def play_nim(k):
    nim = nim_setup(k)
    show_nim(nim)
    random.seed()  # optional, but recommended
    
    # let human player go first ...
    who_moves = "player"
    
    while nim != [0,0,0]:
        if who_moves == "player":
            player_moves(nim)
            who_moves = "computer"
        else:
            computer_moves(nim)
            who_moves = "player"
            # ADD code that switches turn to player
            # ...
            
        print ("These piles of stones remain ... Continue to play!\n")
        show_nim(nim)

    # all piles are empty now ...
    # determine winner; this is the player
    # whose DID NOT make the last move;

    # ADD appropriate condition to replace placeholder value True
    if  who_moves == "player":
        print ("\nComputer took the last stone -- PLAYER WINS :-)\n")
    else:
        print ("\nPlayer took the last stone -- PLAYER LOSES :-(\n")
    return


# to be used in play_nim():
# function interacts with human player to determine
# pile and number of stones the player wants to
# take; empty piles cannont be selected;
# updates game state accordingly

def player_moves(nim):
    pile = int(input("Choose pile [1-3]: "))
    while nim[pile-1] == 0:
        print ("\n Cannot choose an empty pile, try again.")
        pile = int(input("Choose pile [1-3]: "))
    while pile > 3 or pile < 1:
        pile = int(input("\n No such pile, Choose: [1-3]"))
    # ADD -- Optional but recommended: code to sanity-check user
    # input; test whether the chosen pile has zero stones left;
    # keep asking to choose a pile until a pile with >0 stones
    # has been picked;
    # Note: number of stones in pile with number 'pile' is
    # nim[pile-1] 
    # ...
    
    take = int(input("You take how many stones from pile %d? " % pile))
    while take > nim[pile-1] and take > 0:
        print ("\n Take amount must be greater than 0 and no more than the total pile.")
        take = int(input("You take how many stones from pile %d? " % pile))
               
    # ADD -- Optional but recommended: code to sanity-check user
    # input; test whether user takes at least one stone, but no more
    # stones than the chosen pile holds; keep asking until a proper
    # number of stones is given;
    # ...
    nim[pile-1] -= take
    # ADD: code that updates the pile nim[pile-1] to the number of
    # stones after player has taken the indicated number of stones;
    # ...
    
    print ("You took %d stone(s) from pile %d\n" % (take,pile))
    return

# to be used in play_nim():
# function that has computer player make its
# move; it picks a random pile, and given the
# pile, a randome number a stones; empty piles
# can not be selected; updates game state
# accordigly

def computer_moves(nim):
    # ADD code: pick a pile at random but making sure that
    # the pile is not an empty one; e.g., keep
    # doing pile = random.randint(1,3) until
    # nim[pile-1] != 0
    # ...
    pile = random.randint(1,3)
    while nim[pile-1] == 0:
        pile = random.randint(1,3)
    # ADD code: pick a random number of stones that is
    # between 1 and nim[pile-1]
    # ...
    take = random.randint(1, nim[pile-1])
    # ADD code: update the chosen pile to the new number
    # of stones after taking
    # ...
    nim[pile-1] -= take
    print ("Computer took %d stone(s) from pile %d\n" %(take,pile))
    return


    
