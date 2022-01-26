# plain_strips_setupP3.py
# by Kerstin Voigt, new version, for CSE 5120, Fall 2020
# STRIPS planning in 3-blocks world;
# to be used with HW5

# with Python 3 print

import copy
import random

class STRIPS_State():
    def __init__(self,world,goals):
        self.world = world
        self.goals = goals
    
class STRIPS_OP():
    def __init__(self,pre=[],add=[],dels=[], nm="?"):
        self.pres = pre
        self.add = add
        self.dels = dels
        self.name = nm

    def __str__(self):
        outstr="{0}:\n".format(self.name)
        outstr += "pres: {0}\n".format(self.pres)
        outstr += "adds: {0}\n".format(self.adds)
        outstr += "dels: {0}".format(self.dels)
        return outstr

    def __eq__(self,other):
        return self.name == other.name

    
# *****  automatically generating the propositional STRIPS ops ***

# each operator is: move_x_from_y_to_z        
def generate_STRIPS_op(x,y,z):
    pre = gen_preconds(x,y,z)
    adds = gen_adds(x,y,z)
    dels = gen_dels(x,y,z)
    name = "move_{0}_from_{1}_to_{2}".format(x,y,z)
    return STRIPS_OP(pre,adds,dels,name)

# floor is not treated like any of the blocks a,b,c;
# floor is always clear, no adding, no deleting;

def gen_preconds(x,y,z):
    ps = []
    if x != 'floor':
        p = "clear_{0}".format(x)
        ps.append(p)
    if z != 'floor':
        p = "clear_{0}".format(z)
        ps.append(p)
    p = "on_{0}_{1}".format(x,y)
    ps.append(p)
    return ps

def gen_adds(x,y,z):
    a1 = "on_{0}_{1}".format(x,z)
    if y != 'floor':
        a2 = "clear_{0}".format(y)
        return [a1,a2]
    else:
        return [a1]

def gen_dels(x,y,z):
    d1 = "on_{0}_{1}".format(x,y)
    if z != 'floor':
        d2 = "clear_{0}".format(z)
        return [d1,d2]
    else:
        return [d1]

def all_STRIPS_ops(blocks):
    ops = {}
    for b1 in blocks:
        for b2 in blocks + ['floor']:
            for b3 in blocks + ['floor']:
                if b1 != b2 and b1 != b3 and b2 != b3:
                    newop = generate_STRIPS_op(b1,b2,b3)
                    ops[newop.name] = newop
                    #ops.append(generate_STRIPS_op(b1,b2,b3))
    return ops

# operators in 3-blocks world

blocks = ['a','b','c']

ALLOPS = all_STRIPS_ops(blocks)

# World,Goal states
WG1 = STRIPS_State(['on_c_floor','on_b_floor','on_a_c',\
                    'clear_a','clear_b', 'clear_floor'],\
                   ['on_a_floor','on_b_a', 'on_c_b', 'clear_c',\
                    'clear_floor'])


SUSSMAN1 = STRIPS_State(['on_a_floor', 'on_b_floor', 'on_c_a',\
                         'clear_b', 'clear_c', 'clear_floor'],
                        ['on_c_floor','on_b_c', 'on_a_b', 'clear_a',\
                         'clear_floor'])



SUSSMAN2 = STRIPS_State(['on_a_floor', 'on_b_floor', 'on_c_a',\
                         'clear_b', 'clear_c', 'clear_floor'],
                        ['on_b_c', 'on_a_b', 'clear_a',\
                         'on_c_floor','clear_floor'])


SUSSMAN3 = STRIPS_State(['on_a_floor', 'on_b_floor', 'on_c_a',\
                         'clear_b', 'clear_c', 'clear_floor'],
                        ['on_a_b',  'clear_a',\
                         'on_c_floor','on_b_c','clear_floor'])
