# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:49:44 2016

@author: jafcpereira
"""

epsilon = 0.01
square = int(input('Enter a square: '))
guess = square / 2.0
numGuesses = 0

while abs(guess * guess - square) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - square) / (2 * guess))
print('numGuesses = ' + str(numGuesses))
print('Square root of ' + str(square) + ' is about ' + str(guess))