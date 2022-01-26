from plain_strips_setupP3 import *

DEPTH = 100
AT_DEPTH_LIMIT = False

def MY_REC_STRIPS(start, goals):
    checklist = {}
    for g in goals:
        if not g == 'clear_floor':
            checklist[g] = 0
        else:
            checklist[g] = 1
            
    stripsout = rec_strips0(0,start,goals,checklist)
    
    if AT_DEPTH_LIMIT:
        print ("\nRecursion exceed depth limit %d\n\n" % DEPTH)
    else:
        print ("The Plan is:\n")
        print_plan(stripsout)
        print("\n")
    return stripsout
    
def rec_strips0(depth,state,goals,checklist):
    global AT_DEPTH_LIMIT
    AT_DEPTH_LIMIT = False
    
    if goals == [] or goals == ['clear_floor']:
        return [] #empty goals, empty plan
        
    solved = True
    for g in goals:
        if not g in state:
            solved = False
            break;
            
    if solved:
        return [] #no unsat goal instate; empty plan
        
    if depth > DEPTH:
        print ("Recursive Depth exceed limit\n")
        AT_DEPTH_LIMIT = True
        return []
        
    # split off next subgoal from goals
    subgoal = goals[0]
    
    if subgoal == 'clear_floor':
        return rec_strips0(depth,state,goals[1:],checklist)
        
    if subgoal in state:
        print ("[{0}] Subgoal {1} already satisfied\n" .format(depth,subgoal))
        return rec_strips0(depth,state,goals[1:],checklist)
        
    print ("[{0}] Next subgoal: {1}\n".format(depth,subgoal))
    
    prom_ops = find_promising_ops(subgoal)
    
    if prom_ops == []:
        "No applicable operator for subgoal %s\n" % subgoal
        return None
    
    op = random.choice(prom_ops)
    
    print(".... trying operator " + op.name + "\n")
    
    
    op_applies = True
    for p in op.pres:
        if not p in state:
            op_applies = False
            break
            
    #if operator applies to state, add operator to plan
    #and apply plan as for as possible
    #call rec strips on remaining goals
    if op_applies:
        state = apply_op(op,state)
        
        print (".... operator applies, new state:")
        print (state)
        print("\n\n")
        
        for x in checklist.keys():
            if x in state:
                checklist[x] = 1
            else:
                checklist[x] = 0
                if not x in goals:
                    goals = [x] + goals
                    
        return [op] + rec_strips0(depth+1, state,\
                                  goals, checklist)
    else:
        for p in op.pres:
            if not p in state:
                goals = [p] + goals
        return rec_strips0(depth+1, state, goals, checklist)

#if subgoal is on add-list of operator, the operator
#is promising;
def find_promising_ops(subgoal):
    proms = []
    for op in ALLOPS.values():
        for add in op.add:
            if subgoal == add:
                proms.append(op)
    return proms

#delete all on op's delete-list;
#add all on op's add-list
#may assume that op's preconds are met
def apply_op(op,state):
    newstate = copy.deepcopy(state)
    for remove in op.dels:
        newstate.remove(remove)
        print("Removed: " + remove)
    for add in op.add:
        newstate.append(add)
        print("Added: " + add)
    return newstate
    
#apply plan as long as operators apply ...
def apply_plan(plan, state):
    for op in plan:
        state = apply_op(op,state)
    return state
    
#plan is list of STRIPS_OP objects: extract names
#of moves
def print_plan(plan):
    i = 1
    for op in plan:
        print ("%d. %s" % (i, op.name))
        i+=1
    print ("\n")
    return

if __name__ == '__main__':
    random.seed()
    start = SUSSMAN3.world
    goal = SUSSMAN3.goals
    plan = MY_REC_STRIPS(start, goal)
    while len(plan) != 4:
        plan = MY_REC_STRIPS(start,goal)
