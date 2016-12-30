# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:28:40 2016

@author: jafcpereira



In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer 
between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and 
you give it input - is its guess too high or too low? Using bisection search, 
the computer will guess the user's secret number!
"""
low = 0
high = 100
ans = int((low + high) / 2)
guess = ''
print('Please think of a number between 0 and 100!')

while guess != 'c':
    print('Is your secret number {}?'.format(ans))
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to \
indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess == 'l':
        low = ans
        ans = int((low + high) / 2)
    elif guess == 'h':
        high = ans
        ans = int((low + high) / 2)
    elif guess == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: {}'.format(ans))
    
