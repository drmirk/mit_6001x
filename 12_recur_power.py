# -*- coding: utf-8 -*-
"""
instead of sing exponent operator and loop,
use recursive method to exxponent

@author: Ibrahim Rasel
"""
def recurPower(base, exp):
    result = 1
    if(exp > 0):
        result *= base
        return(result * recurPower(base, exp -1))
    else:
        return result
        

print(recurPower(9.4, 0))
print(recurPower(-7.01, 1))
print(recurPower(-5.19, 3))
print(recurPower(6.32, 6))
print(recurPower(-0.96, 5))
print(recurPower(5.68, 10))
print(recurPower(-4.13, 1))
print(recurPower(-6.69, 10))