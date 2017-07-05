# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 00:53:22 2016

@author: ibrahim
"""

def genFib():
       fibn_1 = 1 #fib(n-1)
       fibn_2 = 0 #fib(n-2)
       while True:
              # fib(n) = fib(n-1) + fib(n-2)
              next = fibn_1 + fibn_2
              yield next
              fibn_2 = fibn_1
              fibn_1 = next


test = genFib()

for i in range(10):
    print(test.__next__())
