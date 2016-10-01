# -*- coding: utf-8 -*-
"""
string palindrome

@author: ibrahim
"""
def palindrome(string):
    
    def stripString(string):
        line = ''
        check = "abcdefghijklmnopqrstuvwxyz"
        for i in string:
            if(i in check):
                line = line + i
        return line
                
    def isPalin(string):
        if(len(string) <= 1):
            return True
        if(string[0] == string[-1]):
            isPalin(string[1:-1])
        else:
            return False
    isPalin(stripString(string))
