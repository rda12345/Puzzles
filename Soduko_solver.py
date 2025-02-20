#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Soduko puzzle
"""

## Chapter 1
## Problem 11: Solve a Sudoko

# Defining the Soduko matrix
row1 = [5,3,None,None,7,None,None,None,None]
row2 = [6,None,None,1,9,5,None,None,None]
row3 = [None,9,8,None,None,None,None,6,None]
row4 = [8,None,None,None,6,None,None,None,3]
row5 = [4,None,None,8,None,3,None,None,1]
row6 = [7,None,None,None,2,None,None,None,6]
row7 = [None,6,None,None,None,None,2,8,None]
row8 = [None,None,None,4,1,9,None,None,5]
row9 = [None,None,None,None,8,None,None,7,9]


S = [row1,row2,row3,row4,row5,row6,row7,row8,row9]

# Soduko solver 


def get_sub_square(S,i,j):
    '''
    S: list, a list of lists (9 by 9 matirx)
    i: int, betweeen 1 to 9 defining the row of S[i][j] matrix element
    j: int, betweeen 1 to 9 defining the column of S[i][j] matrix element
    
    Returns: list, the 3 by 3 matrix which includes th element
    '''
    square = []
    m = (i//3)*3
    n = (j//3)*3
    for ii in range(3):
        row = []
        for jj in range(3):
            row.append(S[m+ii][n+jj])
        square.append(row)
        
    return square

   

def Soduko_solver(S):
    
    while any(None in sub for sub in S):
        for i in range(9):
            for j in range(9):
                # Check if the matrix element is empty.
                elem = S[i][j]
                if elem == None:
                    number_list = list(range(1,10))
                    # Check the row
                    for check_elem in S[i][:]:
                        if check_elem != None and check_elem in number_list:
                            number_list.remove(check_elem)
                    # Check column
                    for ii in range(9):
                        check_elem = S[ii][j]
                        if check_elem != None and check_elem in number_list:
                            number_list.remove(check_elem)
                    # Check square 
                    # Find the square
                    # run through all the indicies
                    # clear the numbers from the number list.
                    square = get_sub_square(S,i,j)
                    for row in range(3):
                        for check_elem in square[row][:]:
                            if check_elem != None and check_elem in number_list:
                                number_list.remove(check_elem)
                    
                    # If there is only a single integer left in the number_list
                    # then set the value of S to be that integer.
                    if len(number_list) == 1 :
                        S[i][j] = number_list[0]
                    elif len(number_list) < 1:
                        raise ValueError('There is a problem in the solution.')
    return S


# Soduko test

def Sudoko_test(S):
    # Check all rows
    string = '123456789'
    for i in range(9):
        row = S[i][:]
        # Sorting the vector and then mapping the integers to strings
        row.sort()
        check_string = ''.join(str(integer) for integer in row)
        if check_string != string:
            return False
    # Check columns
    for j in range(9):
        col = []
        for i in range(9):
            col.append(S[i][j])
        col.sort()
        check_string = ''.join(str(integer) for integer in col)
        if check_string != string:
            return False
    # Check squares
    for i in range(0,7,3):
        for j in range(0,7,3):
            square = get_sub_square(S, i, j)
            vec = []
            # Converting the matrix into a vector
            for ii in range(3):
                    vec.extend(square[ii][:])
            # Sorting the vector and converting the integers into strings
            vec.sort() 
            check_string = ''.join(str(integer) for integer in vec)
            if check_string != string:
                return False
    # If all the checks don't go through then all the conditions are met.
    return True



if __name__ == '__main__':   
    print(Soduko_solver(S))    
    print(Sudoko_test(S))

