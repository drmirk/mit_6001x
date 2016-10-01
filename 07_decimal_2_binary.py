# -*- coding: utf-8 -*-
"""
Decimal numbers: 302 = 3*10^2 + 0*10^1 + 2*10^0
Binary numbers: 10011 = 1*2^4 + 0*2^3 + 0*2^2 + 1*2^1 + 1*2^0
binary 10011 = decimal 19

How to convert DECIMAL to BINARY:
1. consider number is X
2. take remainder of X relative to 2, X%2,
    which gives the last binary bit, so, from 010001, gives the last 1
3. now divide X by 2, X//2, get the result in int form
4. now this result is the new X
5. repeat until X is less than 0

@author: ibrahim
"""

num = int(input("Insert a decimal number: "))

if(num < 0):
    isNeg = True
    num = abs(num)
else:
    isNeg = False
    
result = ""

if(num == 0):
    result = "0"
while(num > 0):
    result = str(num%2) + result
    num = num//2
    
if(isNeg):
    result = '-' + result
    
print(result)