#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Euler's project. Problems 1 to 10
"""


import math
"""
Problem 10: Summation of Primes
Find the sum of all the primes below two million.
"""
def gcd(n1,n2):
    """
    Returns the greatest common divisor (int) of integers n2 and n1, where n2 > n1,
    applying Euclid's algorithm, which is based on the fact that gcd(n2,n1) = gcd(n1,r)
    where n2 = n1 * q + r
    """
    while n1:
        r = n2 % n1
        n2 = n1
        n1 = r
    return n2    

def next_prime(n):
    """
    Return the next prime after n, utilizing the Euclid's algorithm to verify
    two numbers are co-prime, and Bertard's postulate which states that
    between n and 2n there exists a prime, for n >= 2.
    """
    if n <= 3:
        raise NameError('n must be greater than 3')
    for i in range(n+1,2*n):
        check = True
        for j in range(2,math.ceil(math.sqrt(n))+1):
            #print(f'j = {j}')
            #print(f'i = {i}')
            #print(f'gcd ={gcd(i,j)}')
            if gcd(i,j) != 1:
                check = False
                break
        if check:
            return i


s = 2 + 3
prime = 5
bound = 2*10**6
while prime < bound:
    s += prime
    prime = next_prime(prime)


print(f'The sum of all the primes bellow {bound} is: {s}')    


"""
Problem 9: Special Pythagorean Triplet
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a * b * c. 
"""
def SPT(num):
    """
    Returns the product of a Pythagorean triplet a,b,c (a^2 + b^2 = c^2)
    such that a + b + c = num
    """
    eps = 10**(-10)
    for a in range(1,num + 1):
        for b in range(1,num + 1):
            c = math.sqrt(a**2 + b**2)
     
            if c % 1 < eps  and (a+b+c) == num:
                return int(a*b*c)
            elif a + b + c > num:
                break

#print(SPT(10**3))


"""
Problem 8: Largest Product in a Series
Find the thirteen adjacent digits in the 
1000-digit number num that have the greatest product. What is the value of this product?
"""
str_num = '73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'


seq_len = 13
prod_max = 0
for i in range(len(str_num)-seq_len+1):
    str_list = list(str_num[i:(i+seq_len)])
    int_list = list(map(int,str_list))
    # checking the product of the integers
    prod = 1
    for integer in int_list:
        prod *= integer
    if prod > prod_max:
        int_list_max = int_list
        prod_max = prod


#print(f'The sequence of integers: {int_list_max}')
#print(f'The product of the integers: {prod_max}')


"""
Problem 7: What is the What is the 10001st prime number?
Solved using the euclid's algorithm to check for the greatest commond divisor (gcd)
for every number between 2 and sqrt(n) we assert if n is a prime
"""
    
def num_prime(n):
    """
    Finds the n's prime number for n > 2
    """
    if n <= 2:
        raise NameError('n must be greater than 2')
    prime = 5
    for i in range(num-3):
        prime = next_prime(prime)
    return prime
    
num = 10001
#print(num_prime(num))



"""
Problem 6: Sum Square Difference
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
N = 100
squares = [x**2 for x in range(N+1)]
result = sum(range(N+1))**2 - sum(squares)
#print(result)


"""
Problem 5: Smallest Multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 with out a remainder.
What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""
def factors(n):
    temp = n
    d = {}
    for i in range(2,n+1):
        while temp % i == 0:
            temp /= i
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1       
        # when the dividing number is greater than temp there is no need to continue iterating.
        if i > temp:
            break
    return d


N = 20
l = list(range(2,N+1))
dictionary = {}
for n in range(2,N):
    # Evaluate the factors of n
    dict_factors_n = factors(n)   # factors returns a dictionary with each factor of times they appear
                            # in the number n
    # Do the factors already appear in the dictionary? if 
    for key in dict_factors_n:
        if key in dictionary:
            # if there are not enough of the factor key modify the number of factors
            if dictionary[key] < dict_factors_n[key]:
                dictionary[key] = dict_factors_n[key]
        # otherwise the factor doesn't appear in the dictionary and we create a new key
        else:
            dictionary[key] = dict_factors_n[key]
            
# go over the dictionary and multiply all the factors
multi = 1
for key in dictionary:
    multi *= key**dictionary[key]   

    
#print(multi)
   

    




"""
Problem 4: Largenst Palindrom Product
A palindrom number reads the same both ways. The largest palindrom made from the prduct of two 2-digit
numbers is 9009 = 91 * 99
Find the largest palindrom made from the procuct of two 3-digit numbers
"""
def palindrom_check(s):
    """ Given a string s it it returns wether the string is a plaindrom or not
    
        Input
            s: str
        Retruns
            bool, True if the s is a polindrom and False otherwise
    """
    # check if the first alpha numeric letter is equal to the last
    # and recurse on the sub problem
    if len(s) < 2:
        return True
    elif s[0] == s[-1]:
        return palindrom_check(s[1:len(s)-1])
    else:
        return False
    
N = 999
l = []
for n in range(N,1,-1):
    for m in range(n,1,-1):
        mult = n * m
        if palindrom_check(str(mult)):
            l.append(mult)
result = max(l)
#print(result)
"""
Problem 3: Largest Prime Factor
What is the largest prime factro of the number 600851475143?
Using a recursive algorithm
"""

def PFS(n):
    """
    returns the set of prime factrors of n.
    
    Input:
        n: int
    
    Returns:
        PFS: list, containing all the prime factors of n
    """
    PFS_list = []
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n%i == 0:
            PFS_list.append(i)
            PFS_list.extend(PFS(n//i))
            return PFS_list
    if len(PFS_list) == 0:
        return [n]

num = 600851475143
PFS_list = PFS(num)
#print(PFS_list)
result = 1
for i in PFS_list:
    result *= i    

#print(result == num)

"""
Problem 2: Even Fibonacci Numbers
Each new tern in the Fibonacci sequence is generated by ading the previous two terms. By considering the terms in
Fibonacci sequence whose values do not exceed for million, find the sum of the even valued terms.
"""
fn_min_2 = 1
fn_min_1 = 2
s = 2
f_n = 0
while f_n < 4*10**6:
    f_n = fn_min_2 + fn_min_1
    fn_min_2 = fn_min_1
    fn_min_1 = f_n
    if f_n%2 == 0:
        s += f_n
#print(s)




"""    
Problem 1: Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,,5,6,9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 10^3.
"""

l = []
for n in range(1,1000):
    if n%3 == 0 or n%5 == 0:
        l.append(n)
#print(sum(l))


