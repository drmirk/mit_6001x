# -*- coding: utf-8 -*-
"""
Instead of using exponential operator, use simple multiplication
and loop to exponent.

@author: Ibrahim Rasel
"""

def iterPower(base, exp):
    result = 1
    while(exp > 0):
        result = result * base
        exp -= 1
    print(result)

        
        
iterPower(9.4, 0)
iterPower(-7.01, 1)
iterPower(-5.19, 3)
iterPower(6.32, 6)
iterPower(-0.96, 5)
iterPower(5.68, 10)
iterPower(-4.13, 1)
iterPower(-6.69, 10)