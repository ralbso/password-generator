#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 16:25:37 2017

@author: Raul
"""

def creditDebt(bal, ann_int_rate, min_pay_rate):
    '''
    bal: current balance due
    ann_int_rate: annual interest rate (in %)
    mon_pay_rate: minimum monthly payment rate (in %)
    
    returns: credit card balance after a year of paying the minimum
    '''
    
    monthlyIntRate = (ann_int_rate / 12.0)
    
    for month in range(12):
        if month == 0:
            '''
            First month calculations.
            minPayment: minimum payment that month based on how much is owed.
            unpaidBal: unpaid balance after making minimum payment.
            newBalDue: updated balance due after monthly interests.
            '''
            minPayment = (bal * min_pay_rate)
            unpaidBal = (bal - minPayment)
            newBalDue = (unpaidBal) + (monthlyIntRate * unpaidBal)
        else:
            '''
            Same as before; however, we take new balance due from first the month. 
            '''
            minPayment = (newBalDue * min_pay_rate)
            unpaidBal = (newBalDue - minPayment)
            newBalDue = (unpaidBal) + (monthlyIntRate * unpaidBal)

    return 'Remaining balance owed: $' + str(round(newBalDue,2))
    
print(creditDebt(1000, 0.24, 0.025))