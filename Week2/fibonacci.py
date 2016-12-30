# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 23:09:57 2016

@author: jafcpereira
"""

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        

fibonacci(4)
        