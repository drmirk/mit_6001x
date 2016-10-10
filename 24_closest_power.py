# -*- coding: utf-8 -*-
"""
Implement a function called closest_power that meets the specifications below.

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
For example,

closest_power(3,12) returns 2
closest_power(4,12) returns 2
closest_power(4,1) returns 0

@author: ibrahim
"""

def closest_power(base, num):
    
    if(num == 1 or base > num):
        return 0
    elif(base == 2):
        while(True):
            root = int(num ** (1/base))
            if(root >= 2):
                base += 1
            else:
                return base - 1
    else:
        root = int(num ** (1/base))
        if(abs(num - (base**root)) <= abs(num - (base**(root+1)))):
            return root
        else:
            return root + 1

    
    
    
    
    
print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))
print(closest_power(2, 192.0)) # 7
print(closest_power(20, 210.0)) # 1
print(closest_power(15, 8.0)) # 0