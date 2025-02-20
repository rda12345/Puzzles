#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution for the tower of Hanoi problem.
The goal is to transfer a tower of n rings by moving the rods one by one according to 
the known rules. 
The fastest number of moves is 2^n.

n: number of rings

Recursive algorithm: 
    1. Mover all the stack of all of the rings except the base to one of the other rods.
    2. Move the base to an empty rod.
    3. Move the stack to the rod of the base.
    
        
"""

## Tower of Hanoi

def move_tower(init,goal,empty,n):
    '''
    Parameters : 
    init : string
        initial rod of the ring tower
    goal : string
        goal rod of the ring tower
    empty : string
        empty rod
    n : int
        number of rings in the tower

    Returns : sequence of moves to solve the problem. 
    '''
    # Base case
    if n == 1:
        print(f'move ring from {init} to {goal}')
    
    else:
        # Move n-1 rings to the empty rod
        move_tower(init,empty ,goal,n-1)
        # Move the base to the goal rod
        move_tower(init,goal,empty,1)
        # Move the n-1 rings to the goal rod on top of the base
        move_tower(empty,goal,init,n-1)
  
# Run the program    
init = 'right'
goal = 'left'
empty = 'mid'

move_tower(init,goal,empty,4)   
   

