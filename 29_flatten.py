# -*- coding: utf-8 -*-
"""
Write a function to flatten a list. The list contains other lists, strings, or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened into [1,'a','cat',2,3,'dog',4,5] (order matters).

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
  

How to think about this problem:
Recursion is extremely useful for this question. You will have to try to flatten every element of the original list. To check whether an element can be flattened, the element must be another object of type list.
"""

def flatten(aList):
    myList = []
    for item in aList:
        if(not isinstance(item, list)):
            myList.append(item)
        else:
            myList += flatten(item)
    return myList
    
li = [[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]]

print(flatten(li))