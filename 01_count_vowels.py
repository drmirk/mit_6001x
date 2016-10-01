# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels
 contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
 For example, if s = 'azcbobobegghakl', program should print:

Number of vowels: 5

@author: ibrahim
"""

s = input("Insert some string: qwre")
count = 0
v = 'aeiou'
for i in s:
    if(i in v):
        count += 1

print('Number of vowels: ', count)