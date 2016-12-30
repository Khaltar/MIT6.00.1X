# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 22:26:56 2016

@author: jafcpereira
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    if aStr == '':
        return False
    if len(aStr) == 1:
        if aStr[0] == char:
            return True
        else:
            return False
    if char == aStr[round(len(aStr) / 2)]:
        return True
    else:
        if char > aStr[round(len(aStr) / 2)]:
            return isIn(char, aStr[round(len(aStr) / 2) + 1 : ])
        else:
            return isIn(char, aStr[0 : round(len(aStr) / 2)])
            
        
