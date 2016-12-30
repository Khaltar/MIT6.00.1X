# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:07:35 2016

@author: jafcpereira
"""

"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s
"""

s = 'azcbobobegghakl'
count = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
print('Number of times bob occurs is: {}'.format(count))
        
