# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:57:43 2016

@author: jafcpereira
"""

def dotProduct(listA, listB):
    return sum([a * b for a,b in zip(listA,listB)])
            