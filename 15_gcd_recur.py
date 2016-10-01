# -*- coding: utf-8 -*-
"""
A clever mathematical trick (due to Euclid)
makes it easy to find greatest common divisors.
Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

@author: Ibrahim Rasel
"""

def gcdRecur(a, b):
    '''
    if(b == 0):
        return a
    elif(a == 0):
        return b

    else:
        k = gcdRecur(b, a%b)
    return k
    '''
    if(b == 0):
        return a
    return gcdRecur(b, a%b)
    
    
     
     
     
m = gcdRecur(24, 75)

print(m)