# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:34:32 2016

@author: jafcpereira
"""
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def f(int1, int2):
    return int1 + int2
    
def dict_interdiff(d1, d2):
    common_keys = d1.keys() & d2.keys()
    diff_keys = d1.keys() ^ d2.keys()
    diff_dict = {}
    for key in diff_keys:
        try:
            diff_dict[key] = d1[key]
        except:
            diff_dict[key] = d2[key]
       
    return ({key : f(d1[key],d2[key]) for key in common_keys}, diff_dict)
            
    