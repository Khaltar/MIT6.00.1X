# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 16:11:25 2016

@author: jafcpereira
"""

def payBalance(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12.0
    balance = balance
    total = 0
    for i in range(1, 13):
        minMonthlyPayment = monthlyPaymentRate * balance
        unpaid_balance = balance - minMonthlyPayment
        total += minMonthlyPayment
        balance = unpaid_balance + (monthlyInterestRate * unpaid_balance)
    print('Remaining balance: {}'.format(round(balance,2)))
    
payBalance(25000, 0.02, 0.01 )
    