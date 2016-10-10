# -*- coding: utf-8 -*-
"""
Fibonacchi recursive code:
def fib(n):
    if n ==1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n - 2)
        
Normally we have 2 base case, so if we have 1 or 2 it is returned.
otherwise a recursive call happens.
Say if iwant 5th fibonacci value. Then to get 5th value first i need the 4th value, to get 4th value i need 3rd value and so on.
5th value is created by adding 4th and 3rd value.
Above function is inefficient cause, for specific value it may calculate other values multiple times.

But we can use dictionary to store values once a number is calculated.
So, one number is only calculated once.

@author: ibrahim
"""

# do a lookup firsst in case already calculated the value
# modify dictinary as progress through function calls

def fib_efficient(n, d):
    global first
    first += 1
    if n in d:
        return(d[n])
    else:
        ans = fib_efficient(n - 1, d) + fib_efficient(n -2, d)
        d[n] = ans
        return ans
        
# Like normal fibonacchi calculation we dont need any base number, instead we can store these base numbers when we created our dictionary first. So, if any value is already in the dictionary it wont be calculated. this is very efficient.
d = {1:1, 2:2}

first = 0

print(fib_efficient(34, d))



def fib(n):
    global second
    second += 1
    if n ==1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n - 2)
        
second = 0
        
print(fib(34))
