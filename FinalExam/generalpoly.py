#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:21:37 2016

@author: jafcpereira
"""


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def result(x):
        lst = L
        k = len(L) - 1
        total = 0
        for num in lst:
            total += num * x**k
            k -= 1
        return total
    
    return result
                