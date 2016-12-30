# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:48:06 2016

@author: jafcpereira
"""

def closest_power(base, num):
    exp = 0
    while base ** exp <= num:
        exp += 1
    if num - base ** (exp - 1)  > base ** (exp) - num:
        return exp
    else:
        return exp - 1