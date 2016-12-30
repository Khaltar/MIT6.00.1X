# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:24:05 2016

@author: jafcpereira
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    for element in L:
        element.reverse()
    L.reverse()