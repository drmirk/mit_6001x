# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that prints the number
of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then
program should print

Number of times bob occurs is: 2


@author: ibrahim
"""

s = input("Inputs string with 'bob' in it: ")

count = 0
ind = 0

while("bob" in s):
    count = count + 1
    ind = s.find("bob")
    s = s[ind+1:]


print('Number of times bob occurs is: ', count)