#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Puzzle from the recitation 11 of 6.006 
"""

## Puzzle
# Extract the k'th smallest element from a min heap
# Solution: Going from the root down, we compare the children of the nodes to
# the next smallest element, which is the minimum element of an auxilary heap.
# We add the keys of larger elements to the auxilary heap.
# Since the auxilary heap contains at most k elements, the algorithm scales as
# O(k*log(k))


## min-heap  

class Heap(object):
    """Min-heap data structure"""
    
    def __init__(self,L = []):
        '''L is a python list'''
        self.L = L
        self.n = len(L)
    
    def __str__(self):
        return str(self.L)
        
    def min_heapify(self,n,i):
        left = 2*i + 1     # left child index
        right = 2*i + 2     # right  child indes
        smallest = i
        
        if left < self.n and self.L[left] < self.L[smallest]:
            smallest = left
            
        if right < self.n and self.L[right] < self.L[smallest]:
            smallest = right
        
        if smallest != i:
            self.L[smallest], self.L[i] = self.L[i], self.L[smallest]
            self.min_heapify(n,smallest)

    def min_heapify_list(self):
        '''Min heapifies the entire list'''        
        for i in range(self.n//2-1,-1,-1):
            self.min_heapify(self.n,i)
            
    def delete_node(self,index):
        '''Deletes the element L[index]. Algorithm swaps L[index] with the last
            leaf and heapifies the list. 
        '''
        if index < self.n:
            self.L[index], self.L[self.n-1] = self.L[self.n-1], self.L[index]
            self.L.pop()
            self.n -= 1
            self.min_heapify_list()
        else:
            print('Index out of range')
            
    def peek(self):
        '''Returns the root node (the maximum for a max heap and the minimum
            for a min-heap).
        '''
        if len(self.L) > 0:
            return self.L[0] 
        return None            
    
    def extract_min(self):
        '''Extracts the maximum item, which is located at the root of the tree,
            assuming the list is max-heapified.
        '''
        temp = self.L[0]
        self.delete_node(0)
        return temp
    
    def insert(self,item):
        '''Inserts the item in the last leaf and heapifies the tree.'''
        self.L.append(item)
        self.n += 1
        self.min_heapify_list()
        
    def check_ri(self,ind):
        """Checks the representation invariant"""
        left = 2*ind + 1
        right = 2*ind + 2
        
        if left < self.n:  
            if self.L[ind] < self.L[left]:
                return self.check_ri(left)
            else:
                raise NameError(f'Left child, {l[left]}, violates the rep. inv.')
        elif right < self.n:
            if self.l[ind] > self.l[right]:
                return self.check_ri(self,right)    
            else:
                raise NameError('Right child, {l[right]}, violates the rep. inv.')
        return True
    
    def kth_smallest(self,k):
        aux_heap = AuxilaryHeap()        
        ind = 0
        aux_heap.insert((self.peek(),0))
        for _ in range(k):
            val, ind = aux_heap.extract_min()
            left = 2*ind + 1     # left child index
            right = 2*ind + 2     # right  child indes
            # extracts the minimum element from the auxilary heap and inserts it's
            # children to the auxilary heap
            if left < self.n:    
                aux_heap.insert((self.L[left],left)) 
            if right < self.n:
                aux_heap.insert((self.L[right],right))
        return (val,ind)
    
    
class AuxilaryHeap(Heap):
    """Auxilary Min-heap data structure. Each node contains a value the index
        of the node in the original heap.
    """
    def __init__(self,L = []):
       Heap.__init__(self,L)
       self.L = [(val,self.L.index(val)) for val in self.L]
       
    def min_heapify(self,n,i):
        left = 2*i + 1     # left child index
        right = 2*i + 2     # right  child indes
        smallest = i
        
        if left < self.n and self.L[left][0] < self.L[smallest][0]:
            smallest = left
            
        if right < self.n and self.L[right][0] < self.L[smallest][0]:
            smallest = right
        
        if smallest != i:
            self.L[smallest], self.L[i] = self.L[i], self.L[smallest]
            self.min_heapify(n,smallest)


            
    def delete_node(self,index):
        '''Deletes the element L[index]. Algorithm swaps L[index] with the last
            leaf and heapifies the list. 
        '''
        if index < self.n:
            self.L[index], self.L[self.n-1] = self.L[self.n-1], self.L[index]
            self.L.pop()
            self.n -= 1
            self.min_heapify_list()
        else:
            print('Index out of range')
            
        
    def check_ri(self,ind):
        """Checks the representation invariant"""
        left = 2*ind + 1
        right = 2*ind + 2
        
        if left < self.n:  
            if self.L[ind][0] < self.L[left][0]:
                return self.check_ri(left)
            else:
                raise NameError(f'Left child, {l[left]}, violates the rep. inv.')
        elif right < self.n:
            if self.l[ind][0] > self.l[right][0]:
                return self.check_ri(self,right)    
            else:
                raise NameError('Right child, {l[right]}, violates the rep. inv.')
        return True

       
        
        




if __name__ == "__main__":
    
    # Heap check

    # k'th_smallest check
    #l = list(range(1,10))
    l = [8,7,2,3,4,1]
    h = Heap(l)
    
    
    h.min_heapify_list()
    #print(h)
    #print(h.check_ri(0))
    
    # auxilary heap check
    aux_h = AuxilaryHeap(l)
    #print(aux_h)
    #print(aux_h.check_ri(0))
    
    ## kth_smallest check
    k = 5
    val, ind = h.kth_smallest(k)
    print(f'kth smallest value: {val}')
    
    
    
    
        
        
    
    
            



