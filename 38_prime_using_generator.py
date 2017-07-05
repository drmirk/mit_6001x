# -*- coding: utf-8 -*-
"""
A candidate number x is prime if (x % p) != 0 for all earlier primes p.

@author: ibrahim
"""

def genPrimes():
       primes = [2]
       cur = 2
       yield cur
       while True:
              try:
                     cur = cur + 1
                     for p in primes:
                            if((cur % p) == 0):
                                   raise ValueError
              except:
                     continue
              else:
                     yield cur
                     primes.append(cur)








pp = genPrimes()

for i in range(10):
    print(pp.__next__())
