#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
house damage riddle:
    There is a line of L houses, each built out of a certain number of bricks.
    If a wind comes and wrecks a house it also wrecks all the houses to the right
    of it with less bricks.
    
    special house: a house with a house to it's right with more bricks and the 
    most right house.
"""


## Warm up problem: a list with only one non-special house.

def find_non_special(l):
    ''' Returns the index of the non-special element closest to the middle of
        of the list.
        If the function is given a list of tuples, the compare operation only
        compares the first element which is the number of bricks.
    '''
    ns_indicies = []
    L = len(l)
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            ns_indicies.append(i)
    if len(ns_indicies) == 0:
        return None
    diff = [abs(x-L//2) for x in ns_indicies]
    ind_min = diff.index(min(diff))
    return ns_indicies[ind_min]

def warmup_damage(houses):
    '''
        Evaluates the damage associated with wrecking any of the houses, for 
        a list with only one non-special house
        input
            houses: list, contains the number of bricks in each house
        returns 
            damage: list, a list of the total damage associated with wrecking each 
                    house (in the same order as the houses)       
    '''
    k = find_non_special(houses)
    print(k)
    if k:
        j = k + 1
    else:
        return houses
    damage = houses[:]
    cumul = 0
    for i in range(k+1):
        print(f'i = {i}')
        print(f'j = {j}')
        while j < len(houses) and houses[i] > houses[j]:
            cumul += houses[j]
            print(f'cumul = {cumul}')
            j += 1
        damage[i] += cumul
    return damage


def merge_sort(l,left,right,ind):
    """ sorts the list according to the ind index of the elements """
    mid = (right + left)//2
    if left == right:
        return [l[mid]]
    else:        
        l1 = merge_sort(l,left,mid,ind)
        l2 = merge_sort(l,mid+1,right,ind)
        return merge(l1,l2,ind)
    
def merge(l1,l2,ind):
    sorted_list = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i][ind] > l2[j][ind]:
            sorted_list.append(l2[j])
            j += 1
        else:
            sorted_list.append(l1[i])
            i += 1
    # insert all the rest of the elements at the end of the sorted list      
    if i == len(l1):
        sorted_list.extend(l2[j:])
    else:
        sorted_list.extend(l1[i:])

    return sorted_list

            
    
    


def damage(houses):
    '''
        Parameters
             houses: list, contains three element lists, containing [number of bricks, damage,original houlse index]
             damage: int, originaly set to be the number of bricks of each house. It gets updated recursively.
        Returns
            sorted_houses: list, contains three element lists, containing [number of bricks,
                                                                           updated damage,original houlse index]
                                 sorted by the brick number.                     
    '''
    k = find_non_special(houses)
 
    # check if lists are sorted by finding if there is a non-special element in the list
    # if sorted then evaluated damage using a two finger algorithm
    if k == None:
        return houses
    else:
        houses1 = damage(houses[:k+1])
        houses2 = damage(houses[k+1:])
        for i in range(len(houses1)):
            j = 0
            cuml = 0
            while j < len(houses2) and houses1[i] > houses2[j]: # The comparison operation compares the first
                                                       # element so no need to add [0]                 
                 cuml += houses2[j][0]
                 j += 1
            houses1[i][1] += cuml
        houses1.extend(houses2)     # adding houses2 to houses1
        # sorte the houses by the number of bricks and return the result
        sorted_houses = merge_sort(houses1,0,len(houses1)-1,0)
        return sorted_houses
            
    
    
    
    # if the lists aren't sorted find the non-special point closest to the middle of the list
    # and recurse
    
    

if __name__ == "__main__":
    
    # The case of only one non-special point
    houses = [1,2,7,1,3,4,5,6]
    print(warmup_damage(houses))
    
    # General array
    houses = [1,2,3,3,1,5,4,1,3]
    comb_houses = list(zip(houses,houses,range(0,len(houses))))
    comb_houses = [list(x) for x in comb_houses]
    total_damage = damage(comb_houses)
    sorted_damage = merge_sort(total_damage,0,len(total_damage)-1,2)
    sorted_damage_list = [x[1] for x in sorted_damage]
    print(sorted_damage_list)
    
    
    
    

    


    
            
                