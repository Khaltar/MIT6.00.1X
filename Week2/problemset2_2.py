# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:39:54 2016

@author: jafcpereira
"""

def minimumPayInAYear(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    minimumPaymentGuess = 0
    balance = balance
    initial_balance = balance
    while balance > 0: #while balance isn't paid off
        #reset balance
        balance = initial_balance
        minimumPaymentGuess += 10
        #calculate remaining balance to pay in 12 months
        for i in range(1, 13): 
            unpaid_balance = balance - minimumPaymentGuess
            balance = unpaid_balance + (monthlyInterestRate * unpaid_balance)
    print('Lowest payment: {}'.format(minimumPaymentGuess))
    
minimumPayInAYear(balance, annualInterestRate)