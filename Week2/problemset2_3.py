# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 17:08:39 2016

@author: jafcpereira
"""

def minimumPayInAYear(balance, annualInterestRate):
    #With Bisection Search
    monthlyInterestRate = annualInterestRate / 12.0
    balance = balance
    initial_balance = balance
    lowerBoundPayment = balance / 12
    upperBoundPayment = (balance * (1 + monthlyInterestRate) ** 12 ) / 12.0
    #While balance isn't paid off
    while round(balance) != 0:
        balance = initial_balance
        # It is always the midway point between upper and lower bound
        minimumPaymentGuess = (upperBoundPayment + lowerBoundPayment) / 2
        #Calculate balance remaining in 12 months
        for i in range(1, 13):
            unpaid_balance = balance - minimumPaymentGuess
            balance = unpaid_balance + (monthlyInterestRate * unpaid_balance)
        #if balance < 0, then the upperbound is too high and should be set to the guess
        if balance < 0:
            upperBoundPayment = minimumPaymentGuess
        #else, lowerBound is too low and should be set to the guess
        else:
            lowerBoundPayment = minimumPaymentGuess
            
    print('Lowest payment: {}'.format(round(minimumPaymentGuess, 2)))
    
minimumPayInAYear(320000, 0.2)