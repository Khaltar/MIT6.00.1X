# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:07:31 2016

@author: jafcpereira
"""
L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    new_list = []
    for element in aList:
        if not isinstance(element, list):
            new_list.append(element)
        else:
            new_list.extend(flatten(element))
    return new_list

flatten(L)