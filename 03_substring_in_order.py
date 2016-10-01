# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring
of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then program should print

Longest substring in alphabetical order is: abc

@author: ibrahim
"""

s = input("Insert a string: ")

maximum = 0
count = 0

max_start = 0
max_end = 1

count_start = 0
count_end = 0

for i in range(len(s)-1):
    if(s[i] <= s[i+1]):
        count_end = i+1
        count = count + 1
        if(maximum < count):
            maximum = count
            max_start = count_start
            max_end = count_end + 1
    else:
        count = 0
        count_start = i + 1
        count_end = 0
        
print("Longest substring in alphabetical order is: ", s[max_start:max_end])
