#Damon Nutter
#006315383
#CSE5120
#September 2020
#jugs.py

#Uses generic A* alg to solve jugg puzzle

import random
import copy

MAX1 = 3
MAX2 = 4
jugs = [0,0]
GOALJUGS = [0,2]

#Print the jugs
def show_jugs(jugs):
    if jugs == None:
        return
    print("3L:", end ='')
    for i in range (0, jugs[0]):
        print("~", end ='')
    print("\n")
    print("4L:", end ='')
    for i in range(0, jugs[1]):
        print("~", end ='')
    print("\n")
    return

#compare current jugs state to goal state
def jug_goal_fct(jugs, GOALJUGS):
    if not jugs == GOALJUGS:
        return False
    return True
#return 0 because no eval function exists
def jug_eval_fct(jugs, GOALJUGS):
    return 0
#try all move functions and collect all non-None succ states
def jugs_successor_fct(jugs):
    succs = []
    moves = [fill_3_jugg(jugs),fill_4_jugg(jugs),\
             pour_3_jugg(jugs),pour_4_jugg(jugs),\
             pour_3_to_4(jugs),pour_4_to_3(jugs)]
    for x in moves:
        if not x == None:
            succs.append(x)
    return succs
def fill_3_jugg(jugs):
    newjugs = copy.deepcopy(jugs)
    newjugs[0] = MAX1
    return newjugs
def fill_4_jugg(jugs):
    newjugs = copy.deepcopy(jugs)
    newjugs[1]=MAX2
    return newjugs
def pour_3_jugg(jugs):
    newjugs = copy.deepcopy(jugs)
    newjugs[0]=0
    return newjugs
def pour_4_jugg(jugs):
    newjugs = copy.deepcopy(jugs)
    newjugs[1]=0
    return newjugs
def pour_3_to_4(jugs):
    #make a copy
    newjugs = copy.deepcopy(jugs)
    #no overflow
    if (newjugs[0] + newjugs[1] <= MAX2):
        newjugs[1] = newjugs[0] + newjugs[1]
        newjugs[0] = 0
    #overflow
    else:
        newjugs[0] = newjugs[0] - MAX2 + newjugs[1]
        newjugs[1] = MAX2
    return newjugs
def pour_4_to_3(jugs):
    #make a copy
    newjugs = copy.deepcopy(jugs)
    #no overflow
    if (newjugs[0] + newjugs[1] <= MAX1):
        newjugs[0] = newjugs[0] + newjugs[1]
        newjugs[1] = 0
    #overflow
    else:
        newjugs[1] = newjugs[1] - MAX1 + newjugs[0]
        newjugs[0] = MAX1
    return newjugs        
    
