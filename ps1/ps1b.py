# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:03:24 2020

@author: Vivek_Verma
"""

total_cost = float(input('Enter Total cost of your dream home : '))
annual_salary = float(input('Enter starting annual salary : '))
portion_saved = float(input('Enter percent of your salary to save, as decimal : '))
semi_annual_raise = float(input('Enter the semiannual raise, as a decimal : '))
r = 0.04
portion_down_payment = 0.25
current_savings = 0
months = 0

while current_savings <= total_cost*portion_down_payment:
    if (months%6 == 0) and (months != 0)  :
        annual_salary += annual_salary*semi_annual_raise
    current_savings = current_savings + (current_savings*r)/12 + (annual_salary/12)*portion_saved
    months += 1 
print(months)