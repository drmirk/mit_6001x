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


How to convert fractional DECIMAL to BINARY:
1. find a power of 2
2. multiply that with the fraction
3. we will get a whole number
4. if not found the whole number, find another power of 2
5. finally take that whole number and convert it normally
6. and then again divide that converted binary with the same 
    power of 2 (shift right, so if that power was 3 shift right 3,
    so 11 becomes 011, if power 8 shift right 8)
    
    
    
Some implications:
- If there is no integer P such that X*(2**P) is a whole
    number, then internal representation is always an approximation
- Suggest that testing equality of floats is not exact
    - Use abs(x-y) < some small number, rather tha x == y
- Why does print(0.1) return 0.1, if not exact?
    - Because Python designers set it up this way to automatically
        round

@author: ibrahim
"""
x = float(input('Enter a decimal number between 0 and 1: '))

p = 0
while ((2**p)*x)%1 != 0:
    print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
