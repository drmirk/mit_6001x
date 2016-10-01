# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 01:06:12 2016

@author: Ibrahim Rasel
"""
n = int(input("Insert stack size: "))


def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

Towers(n, 'Start', 'End', 'Middle')