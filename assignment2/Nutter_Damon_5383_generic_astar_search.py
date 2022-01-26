#Damon Nutter
#006315383
#CSE5120
#September 2020
#Generic A* alg for puzzle solving

import random
import operator
from puzz8 import *
from jugs import *

class Node:
    def __init__(self, state = None, path = [], depth = 0, evalue = None):
        self.thestate = state
        self.thepath = path
        self.thedepth = depth
        self.theeval = evalue

    def __eq__(self, other):
        return self.thestate == other.thestate

def ASTAR_SEARCH(start, target,GOAL_FCT,EVAL_FCT,SUCCESSOR_FCT):
    open = [Node(start,[start],0,EVAL_FCT(start,target))]
    closed = []
    steps = 0
    while open != []:
        nxt = open[0]
        open = open[1:]
        nxtstate = nxt.thestate #unpack the node
        nxtpath = nxt.thepath
        nxteval = nxt.theeval
        nxtdpth = nxt.thedepth

        if GOAL_FCT(nxtstate,target):
            print ("GOAL FOUND:")
            print ("State: %s" % nxtstate)
            print ("PathL: %d" % len(nxtpath))
            print ("Steps: %d\n" % steps)
            return [nxtstate, nxtpath]
        if nxt in closed:
            continue
        closed.append(nxt)

        succ = SUCCESSOR_FCT(nxtstate)
        random.shuffle(succ)
        for x in succ:
            xcost = EVAL_FCT(x,target)
            newnode = Node(x,addpath(nxtpath,x),nxtdpth+1,xcost+nxtdpth+1)
            #check whether newstate[0] (or, x) is
            #already on open or closed with shorter
            #path; if so, do not bother to put on open;
            keeper = True
            for c in closed:
                if newnode.thestate == c.thestate and\
                   len(newnode.thepath) >= len(c.thepath):
                    keeper = False
                    break
            if not keeper:
                continue
            for op in open:
                if newnode.thestate == op.thestate and\
                   len(newnode.thepath) >= len(op.thepath):
                    keeper = False
                    break
            if keeper:
                open.append(newnode)
        open.sort(key= operator.attrgetter('theeval'))
        steps+=1
    return None

#utility function
def addpath(path,x):
    newpath = path[:]
    newpath.append(x)
    return newpath

if __name__ == '__main__':
    random.seed()

    goalfct = jug_goal_fct#puzz8_goal_fct
    evalfct = jug_eval_fct#puzz8_eval_fct
    succfct = jugs_successor_fct#puzz8_successor_fct
    showfct = show_jugs#show_puzz8
    start_state = jugs#puzzE
    goal_state = GOALJUGS#GOAL
    solnA = ASTAR_SEARCH(start_state,goal_state,goalfct,evalfct,succfct)   
    i=0
    #print(solnA)
    for p in solnA[1]:
        print ("\n%d. move yields: " %i)
        showfct(p)
        i+=1
        
