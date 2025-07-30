#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DP basic problems taken from
 https://www.geeksforgeeks.org/competitive-programming/dynamic-programming/
"""

# Puzzle 1
# Fibonacci numbers
# Bottom up approach: O(n) time and O(1) space 

def Fibonacci(n):
    Fib_1 = 1
    Fib_2 = 1
    for _ in range(n-2):
        Fib = Fib_1 + Fib_2
        Fib_2 = Fib_1
        Fib_1 = Fib
    return Fib


# Check
#res = Fibonacci(10)   
#print(res)


# Puzzle 2
# There are n stairs, and a person standing at the bottom wants to climb stairs 
# to reach the top. The person can climb either 1 stair or 2 stairs at a time,
# the task is to count the number of ways that a person can reach at the top.


# Solution: writting up the four first solutions
# 1
# 1,1 ; 2
# 1,2 ; 1,1,1; 2,1
# 1,1,2 ; 2,2 ; 1,2,1 ; 1,1,1,1 ; 2,1,1 
# one can notice that the options for  n = 4 are obtained
# by adding 2 to all the options of n = 2 and one to all the options of n = 3.
# Similarly if dp is the number of ways to reach the n'th stair is given by 
# dp[n] = dp[n-2] +dp[n-1].
# The boundary condition is a bit different, where dp[n] = Fibonacci[n+1]
 

# Puzzle 3
# A child is running up a staircase with n steps and can hop either 1 step,
# 2 steps, or 3 steps at a time. The task is to implement a method to count
# how many possible ways the child can run up the stairs.

# Solution: writting up the four first solutions
# 1
# 1,1 ; 2
# 1,2 ; 1,1,1; 2,1 ; 3
# 3,1 ; 1,1,2 ; 2,2 ; 1,2,1 ; 1,1,1,1 ; 2,1,1 ; 3,1
# one can notice that the options for  n = 4 are obtained
# by adding 1 to all the options of n = 3, 2 to all the options of n = 2 and 3 
# to all the options of n = 1.
# Similarly if dp is the number of ways to reach the n'th stair is given by 
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3].


# Applying a bottom up approach we have (for n > 3)
# Complexity: O(n) time O(1) space
def num_ways(n):
    dp1 = 1
    dp2 = 2
    dp3 = 4
    for _ in range(n-3):
        dp = dp1 + dp2 + dp3 
        dp2 = dp1
        dp3 = dp2
        dp1 = dp
    return dp


# Check
#res = num_ways(4)
#print(res)

# Puzzle 4
# Given an array of integers cost[] of length n, where cost[i] is the cost of 
# the ith step on a staircase. Once the cost is paid, we can either climb one or two steps.
# We can either start from the step with index 0, or the step with index 1. The task is
# to find the minimum cost to reach the top.

# Solution: let dp[i] be the minimum cost of reaching the i'th step, we can 
# reach the i'th step by climbing one or two steps, therefore, the optimized
# strategy is given by dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])



# Applying a bottom up approach we have 
# Complexity: O(n) time and O(n) space (the number of subproblems is O(n) and
# each problem takes O(1) time). 

def total_cost(cost):
    n = len(cost)+1
    dp = [0]*n
    for i in range(2,n):
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    return dp[n-1]


# Improvement on the space complexity: O(1) space
def total_cost2(cost):
    n = len(cost)+1
    dp1 = 0
    dp2 = 0
    for i in range(2,n):
        dp = min(dp1 + cost[i-1], dp2 + cost[i-2])
        dp2 = dp1
        dp1 = dp        
    return dp

# Check
#cost = [10,15,20]
#cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#res = total_cost2(cost)
#print(res)


# Puzzle 5 - Maximize the number of segments of length x, y and z
# Given a rod of length n, the task is to cut the rod in such a way that the total number of segments of length x, y, and z is maximized. The segments can only be of length x, y, and z. 
# Note: If no segment can be cut then return 0.

# Solution1: let the state be dp[i,j], where we are have a j length rod and we are
# deciding if to cut the rod into k pieces of length i and j-i*k or not cut at
# all and go to the state dp[i+1,j].
# The transition of the state is dp[i,j] = max_k(dp[i,j-i*k]+k,dp[i-1,j])
# I apply the bottom up approach.

# Complexity: let n be the length of the rod, since x,y,z are integers
# k is O(n), j is also O(n) while i obtains only 3 values,
# it is therefore O(1). Therefore, the number of subproblems is O(n)
# and each subproblem takes O(n) time to solve.
# Overall, the complexity is O(n^2).





def cut(n,lengths):
    num_cuts = len(lengths)
    dp = {}
    parents = {}
    # Initialize the result for sizes up to n where no cut is made.
    for num in range(n+1):
        dp[0,num] = 0
    
    # Iterate over the possible sizes
    for j in range(n+1):        
        # Iterate over the items + and additional auxilary item 
        for i in range(1,num_cuts+1):
            dp[i,j] = dp[i-1,j]
            parents[i,j] = (i-1,j)
            max_num = dp[i,j]
            k = 0
            size = lengths[i-1]
            #print(f'i = {i}, size = {size}')
            # incrementing k (the number of cuts of length i)
            while j - size*k >= 0:
                new_max = dp[i,j-size*k]+k 
                if  new_max > max_num:
                    max_num = new_max
                k += 1
            dp[i,j] = max(max_num,new_max)
            parents[i,j] = (i-1,j-size*(k-1))
    # Organizing the results
    states = []
    i = num_cuts
    j = n
    for _ in range(num_cuts):
        states.append((i,j))
        i,j = parents[i,j]
    return (dp[num_cuts,n],states)


# Check 
#n = 11
#x,y,z = 5,3,2
#lengths = [x,y,z]
#maximum, states = cut(n,lengths)
#print(f'Maximum number of cuts: {maximum}')
#print(f'States: {states}')




# Solution2: let dp[j] be the number of cuts made to a rod of length j. 
# Each time you decide which if to perform a certain cut.
# The transition of the state is given dp[i] = max_w(dp[i-w]+1,dp[i])
# where dp[i] is initiated to 0, and if no cut can be done dp[i] = -1.
# We apply the bottom up approach.

# Complexity: let n be the length of the rod, there are n subproblems and each
# one takes O(1) time to solve, therefore the complexity is O(n).

def cut2(n,lengths):
    dp = [0]*(n+1)
    for i in range(n+1):
        for w in lengths:
            if i >= w and dp[i-w] != -1:
                dp[i] = max(dp[i],dp[i-w]+1)
    # If no cut was possible set dp[i] = -1
    if dp[i] == 0:
        dp[i] = -1
    # If no cut is possible for dp[n], set dp[n] = 0
    if dp[n] == -1:
        dp[n] = 0
    
    return dp[n]

# Check 
#n = 11
#x,y,z = 5,3,2
#lengths = [x,y,z]
#maximum = cut2(n,lengths)
#print(f'Maximum number of cuts: {maximum}')




# Puzzle 6 - Program for nth Catalan Number
# The formula for the n'th Catalan number is C_n = (2n!)/(n!(n+1)!)
# It can easily be shown that C_n = ((2*(2n-1))/(n+1))*C_(n+1)
# with boundary condition C_0 = 1

# Solution: a simple iteration from 0 to n gives the desired result.

# Complexity: the iteration takes O(n) time.

def Catalan(n):
    C_i = 1    
    for i in range(1,n+1):
        C_i = (2*(2*i - 1)/(i+1))*C_i
    return int(C_i)

# Check
#n = 8
#print(Catalan(n))

    
# Puzzle 7 - Number of Unique BST with n Keys

# Solution: The answer is given by the n'th Catalan number. This can be proven by noticing
# that for a tree with i-1 keys in the left sub tree and n-i nodes in the right 
# subtree, the number of unique configuration in the left subtree is C[n] and the
# number of unique configurations for the right of the tree is C[n-i]. Therefore
# the total number of configurations, is a sum C[n] = sum_{i=1,...,n}C[i-1]C[n-i]
# which the recursive relation for the Catalan numbers.


# Puzzle 8 - Number of ways of Triangulation for a Polygon
# Given a convex polygon with n sides. The task is to calculate the number of ways 
# in which triangles can be formed by connecting vertices with non-crossing line segments.

# Solution: similarly to the last question, we can describe the solution in terms of 
# a recursion relation. Let C[n] be the number of ways in which traingles can be
# formed. We consider a polygon with n vertices and cut the poligon
# to two poligons one with 3+i sides and one with n-i-1, for this cut the total number
# of unique ways is  C[i+3]*C[n-i-1], with i=0,...,n-3. Considering all the cuts, we have
# C[n] = sum_{i=0,...,n-3}, with boundary condition C[2] = 1, C[3] = 1.
# Defining m = n - 2, we have C[m] = sum{j=0,...m-1}C[j]C[n-j-1] which is the
# recursion relation of the Catalan numbers.


# Puzzle 8 - Minimum Sum Path in a Triangle
# Given a triangular array, find the minimum path sum from top to bottom.
# For each step, we can move to the adjacent numbers of the row below. i.e.,
# if we are on an index i of the current row, we can move to either index i or 
# index i + 1 on the next row.

# Solution: Let the state be dp[i,j] the minimum sum of the path ending in (i,j)
# array element. The transition between the states is given by
# dp[i,j] = min(dp[i-1,j],dp[i-1,j-1]+A[i,j]


# Complexity: If the number of rows in the triangle is n.
# There are O(n^2) subproblems and each one takes O(1) time, therefore
# the algorithm takes O(n^2) time.

def minSumPath(A):
    dp_prev = [float('inf'),A[0][0]]
    for i in range(1,len(A)):
        dp = [float('inf')]*(len(A[i])+1)
        for j in range(1,len(A[i])):    
            dp[j] = min(dp_prev[j-1],dp_prev[j]) + A[i][j-1]
        #The last element of the row has a different recursion relation than the rest
        dp[j+1] = dp_prev[j] + A[i][j]
        dp_prev= dp
    return min(dp)

# Check 
#triangle =  [[2],[3, 7],[8, 5, 6],[6, 1, 9, 3]]
#triangle =  [[3],[6, 9],[8, 7, 1],[9, 6, 8, 2]]
#res = minSumPath(triangle)
#print(res)
        

# Puzzle 9 - Minimum perfect squares to add that sum to given number.
# Given a positive integer n, the task is to find the minimum number of squares
# that sum to n.

# Solution: dp[i,j], the number of squares involving the the numbers i,...,floor(sqrt(j))
# which sum up to j.
# We have the recursion relation: dp[i,j] = max_{k=0,...}(dp[i+1,j-k*i^2])

# Complexity: there are O(n^2) subproblems (all the options of i and j), each
# subproblem takes possibly n times  (there might be n options for k, for example
# if n is prime), therefore the total time complexity is O(n^3). 
import math
import numpy as np
def minPerfectSquare(n):
    # Initializing the dp array to infinite values
    dp =np.array([[float('inf')]*(n+1)]*(n+1))
    
    # Setting the boundary conditions
    for i in range(n):
        dp[i,0] = 0
    
    # Iterating over the total sum
    for j in range(0,n+1):
        # Iterating over the elements 
        for i in range(math.ceil(math.sqrt(j)),0,-1):
            choices = []
            if i**2 == j:
                #Boundary conditions
                dp[i,j] = 1
            elif i**2 < j:
                k = 0
                while j-k*i**2 >= 0:
                    choices.append(dp[i+1,j-k*i**2]+k)                         
                    k += 1
                if choices:
                    dp[i,j] = min(choices)
                else:
                    dp[i,j] = 0
    return int(dp[1,n])

# Check
#n = 15
#res = minPerfectSquare(n)
#print(res)
                    
                        
                    
                    
                
            

# Puzzle 10 - Bell Numbers (Number of ways to Partition a Set)
# Given a set of n elements, find the number of ways of partitioning it. 

# Solution: we can consider the S(n,k) the number of ways to partition n elements
# to k sets. Each time we add a new element we can add it to any of the k sets of 
# the S(n-1,k) sets or add the new element as an new set to the S(n-1,k-1) set.
# Therefore S(n,k) = k*S(n-1,k) + S(n-1,k-1), and the total number of partitions are
# sum_{k = 1,...,n} S(n,k). The implementation utilizes memoization, also the code
# can be easily extended to a bottom up approach, utilizing an array.

# Complexity: There are O(n^2) subproblems and each one takes O(1) time, therefore
# the algorithm takes O(n^2) time.

def BellNumber(n):
    S = {}
    #Setting boundary conditions
    for i in range(n):
        S[i,0] = 0
    S[0,1],S[1,1] = 1,1
    
    if n == 0 or n == 1:
        return 1
    for m in range(1,n+1):
        for k in range(1,m+1):
            if k < m:
                S[m,k] = k * S[m-1,k] + S[m-1,k-1]
            elif k == m:
                S[m,k] = 1
    s = 0
    for k in range(1,n+1):
        s += S[n,k]
    return s

#check 
#res = BellNumber(7)
#print(res)
    

# Puzzle 11 - Binomial Coefficient
# Given an integer values n and k, the task is to find the value of Binomial
# Coefficient C(n, k).

# Solution: Writing the polynomial explicitly, one can infer that the
# binomial coefficient is given by C(n,k) = choose(n,k).
# Therefore we have the recursion relation C(n,k) = n!/((n-k)!k!) = ((n-k+1)/k)*C(n,k-1)
# In addition, for n >= k+1, C(n,k) = (n/(n-k))*C(n-1,k)


# Complexity: There are O(n^2) subproblems and each one takes O(1) time, therefore
# the algorithm takes O(n^2) time.

def BinomialCoeff(n,k):
    C = {}
    C[1,1] = 1
    for m in range(2,n+1):
        C[m,1] = (m/(m-1))*C[m-1,1] 
        for l in range(2,m):
            C[m,l] = ((m-l+1)/l)*C[m,l-1]
    return int(C[n,k])
            
#Check
#n = 6
#k = 3
#res = BinomialCoeff(n, k)
#print(res)  

# Puzzle 12 - Program to Print Pascal's Triangle
# Given an integer n, the task is to find the first n rows of Pascal's triangle.
# Pascal's triangle is a triangular array of binomial coefficients. 

# Solution: the boundary element is always 1 and the internal element in the i'th
# row and j'th "column" is given by triangle[i][j] = triangle[i-1][j-1]+triangle[i-1][j].

# Complexity: There are O(n^2) subproblems and each one takes O(1) time, therefore
# the algorithm takes O(n^2) time.


def PascalTriangle(n):
    triangle =[[1]]
    for i in range (1,n):
       row = [1]*(i+1)
       for j in range(1,i):
           row[j] = triangle[i-1][j-1] + triangle[i-1][j]
       triangle.append(row)
    return triangle

#Check
#res = PascalTriangle(7)
#print(res)










