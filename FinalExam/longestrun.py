#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 11:45:08 2016

@author: jafcpereira
"""

    

def pos_increasing(L):
    best_run_pos = []
    longest_run = [L[0]]
    for k in range(len(L) - 1):
        if L[k+1] >= L[k]:
            longest_run.append(L[k+1])
            if len(longest_run) > len(best_run_pos):
                best_run_pos = longest_run[:]
        elif L[k] > L[k + 1]:
            longest_run = [L[k + 1]]
    return best_run_pos
    
def neg_increasing(L):
    best_run_neg = []
    longest_run = [L[0]]
    for k in range(len(L) - 1):
        if L[k+1] <= L[k]:
            longest_run.append(L[k+1])
            if len(longest_run) > len(best_run_neg):
                best_run_neg = longest_run[:]
        elif L[k] < L[k+1]:
            longest_run = [L[k + 1]]
    return best_run_neg
    
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    best_run_pos = pos_increasing(L)
    best_run_neg = neg_increasing(L)
    if len(best_run_neg) > len(best_run_pos):
        return sum(best_run_neg)
    elif len(best_run_neg) < len(best_run_pos):
        return sum(best_run_pos)
    else:
        if L.index(best_run_pos[0]) > L.index(best_run_neg[0]):
            return sum(best_run_neg)
        elif L.index(best_run_pos[0]) < L.index(best_run_neg[0]):
            return sum(best_run_pos)
        else:
            return sum(best_run_pos)

