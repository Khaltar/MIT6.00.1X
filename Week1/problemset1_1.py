# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:24:03 2016

@author: jafcpereira
"""

"""
Write a program that counts up the number of vowels contained in the string s
"""

s = 'azcbobobegghakl'

num_vowels = 0
for char in s:
    if char in 'aeiou':
        num_vowels += 1
print('Number of vowels: {}'.format(num_vowels))
    