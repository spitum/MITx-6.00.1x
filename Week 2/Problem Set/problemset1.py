'''
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy
'''

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#print(round(b1,2),round(b2,2))
months = 1
while months <= 12:
    minpayment  = balance * monthlyPaymentRate
    ub = balance - minpayment
    interest = (annualInterestRate/12)*ub
    balance = ub + interest
    months +=1
print('Remaining balance: ' + str(round(balance,2)))
