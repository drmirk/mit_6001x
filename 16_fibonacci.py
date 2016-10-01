# -*- coding: utf-8 -*-
"""
there are a pair of rabbits, a male and a female.
After first month they become mature, and start having sex
after second month they produce anther pair of male and female
so, at third month original female produces another pair
and at the same time their first born becomes mature
after fourth month, original produces another, first born 
produces one pair and originals's second born becomes mature

and so on

what is the number after one year.

month       females
0           1
1           1
2           2
3           3
4           5
6           13

so, females(n) = females(n-1) + females(n-2)



@author: ibrahim
"""


def fib(x):
    if(x == 0 or x == 1):
        return 1
    else:
        return fib(x-1) + fib(x-2)