#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Puzzle from the recitation 11 of 6.006 
"""

## Puzzle:
# Given a shifted sorted list such as [7,8,9,1,2,5] perform a search in time O(log(N))
# Solution find the jump and than perform a binary search on each of the sorted arrays


# First way: performing a binary search under the condition that the low_ind > upper_ind
# until low_ind + 1 = upper_ind

def find_jump(l,low,high):
    """
    Returns the index (int) in the list right after the jump for a sorted shifted list 
    
    Input: 
        l: list
        low: int, first index of the list
        high: int, last index of the list
    """
    mid = low + (high - low)//2
    
    if high - low == 1:
        return high
    if l[low] > l[mid]:
        return find_jump(l,low,mid)
    else:
        return find_jump(l,mid,high)

def BS(l,low,high,k):
    """Performs a binary search for the key k in the list l[low:high+1].
       Returns the index of the object in the list or None.
       
       Input: 
           l: list
           low: int, first index of the list
           high: int, last index of the list
    """
    #print(f'sorted list: {l[low:high+1]}')
    
    mid = low + (high - low)//2
    if l[mid] == k:
        return mid
    elif mid == low:
        if l[high] == k:
            return high
        return None
    elif l[mid] < k:
        return BS(l,mid,high,k)
    else:
        return BS(l,low,mid,k)
    
    
def BS_shift(l,k):
    """Performs a binary search of a shifted list of the key k.
       Returns the index of the object in the list or None.
       
       Input: 
           l: list
    """
    jump_ind = find_jump(l,0,len(l)-1)
    print(jump_ind)
    return BS(l,0,jump_ind-1,k) or BS(l,jump_ind,len(l)-1,k)

    
    


if __name__ == '__main__':
    
    """
    ## find_jump check
    l = [4,5,6,7,1,2]
    k = find_jump(l,0,len(l)-1)
    print(k)
    

    # binary search check
    #l = [1,2,4,6,7,8,9]
    l = [1,2]
    result = BS(l,0,len(l)-1,3)
    print(result)
        
    """
    # BS_shift check
    l = [4,5,6,7,1,2]
    result = BS_shift(l,6)
    print(result)
