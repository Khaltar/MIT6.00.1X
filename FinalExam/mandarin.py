#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 22:00:50 2016

@author: jafcpereira
"""

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
          
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    int_num = int(us_num)
    if int_num >= 0 and int_num <= 10:
        return trans[str(int_num)]
    elif int_num >= 11 and int_num <= 19:
        return trans['10'] + ' ' + trans[str(int_num % 10)]
    elif int_num % 10 == 0:
        return trans[str(int_num // 10)] + ' ' + trans['10']
    else:
        return trans[str(int_num // 10)] + ' ' + trans['10'] + ' ' + trans[str(int_num % 10)]
    