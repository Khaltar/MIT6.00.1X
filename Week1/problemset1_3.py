# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:16:52 2016

@author: jafcpereira
"""

"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur
in alphabetical order.
"""

s = 'azcbobobegghakl'
longest = s[0]
subString = s[0]

for i in range(1, len(s)):
    if s[i] >= subString[-1]:
        subString += s[i]
        if len(subString) > len(longest):
            longest = subString
    else:
        subString = s[i]
print('Longest substring in alphabetical order is: {}'.format(longest))


    