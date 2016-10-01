# -*- coding: utf-8 -*-
"""
Write an iterative function, gcdIter(a, b),
that implements this idea. One easy way to do
this is to begin with a test value equal to the
smaller of the two input arguments, and iteratively
reduce this test value by 1 until you either reach a
case where the test divides both a and b without remainder,
or you reach 1.

@author: Ibrahim Rasel
"""
'''
def gcdIter(a, b):
    smaller = b
    if(a < b):
        smaller = a
    while(smaller >= 1):
        if((a % smaller == 0) and (b% smaller ==0)):
            return smaller
        else:
            smaller -= 1
            
print(gcdIter(17, 12))
'''

def gcdIter(a, b):
    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue