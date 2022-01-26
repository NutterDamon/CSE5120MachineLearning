#Damon Nutter
#006315383
#Interact_resolve adapted from lecture and 2 new functions
#included: print_list(x) and interact_resolve(x)

CLS = [['notP', 'notQ', 'R'], ['P', 'R'], ['Q', 'R'], ['notR']]

CHEM = [['notCO2', 'notH2O', 'H2CO3'],['notC', 'notO2', 'CO2'],\
        ['notMgO', 'notH2', 'Mg'], ['notMgO', 'notH2', 'H2O'],\
        ['MgO'], ['H2'], ['O2'], ['C'], ['notH2CO3']]

GOV = [['T', 'notE', 'D'], ['notT', 'C'], ['E', 'notD', 'I'],\
       ['notG', 'notD', 'I'], ['T', 'C', 'notD', 'G'], ['notC'],\
       ['notI', 'notG'], ['D'], ['E']]
Q10 = [['P', 'Q'],['P','notQ'],['notP','Q'],['notQ','notP'],['notP','notQ']]
def print_list(x):
    i = 0
    for e in x:
        i+=1
        print("[%d] %s" %(i, e))

def interact_resolve(x):
    res = 0
    while res != []:
        print_list(x)
        print("Pick two clauses by their number: ")
        choice1 = input("First clause: ")      
        choice2 = input("Second clause: ")
        c1 = x[int(choice1) - 1]
        c2 = x[int(choice2) - 1]
        res = try_resolvent(1, c1, c2)
        print("Adding new clause %s" %(res))
        x.append(res)
    print("UNSATISFIABLE :D")
    
def try_resolvent(count,c1,c2):
    res = None
    for lit1 in c1:
        for lit2 in c2:
            if is_complement(lit1,lit2):
                print ("\n[%d.] Resolving %s and %s ..." %(count,c1,c2))
                print ("... found compl lits (%s,%s)" %(lit1,lit2))
                res = c1[:]
                res.remove(lit1)
                for x in c2:
                    if not x in res and x!= lit2:
                        if complement(x) in res:
                            return True
                        else:
                            res.append(x)
                return res
    print ("No resolvent")
    return res

def is_complement(x,y):
    if len(x) >= 4 and x[:3] == 'not':
        return x[3:] == y
    elif len(y) >= 4 and y[:3] == 'not':
        return x == y[3:]
    else:
        return False

def complement(x):
    if len(x) >= 4 and x[:3] == 'not':
        return x[3:]
    else:
        return 'not'+x

#c1 same as c2, if both contain the same elements, but possibly in
#different order; iterate over one and test whether it is present in
#the other;

def same_clause(c1,c2):
    if not len(c1) == len(c2):
        return False
    for x in c1:
        if not x in c2:
            return False
        return True
