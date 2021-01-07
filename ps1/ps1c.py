# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:06:23 2020

@author: Vivek_Verma
"""
st_annual_salary = float(input("Enter your starting annual salary: "))
semi_ann_raise = 0.07
r = 0.04
down_payment = 0.25
total_cost = 1000000
time = 36 
epsilon = 100
ps_high = 10000
ps_low = 0 
ps_guess = (ps_high + ps_low)//2
itr = 0 
cond = True 
possible = True

while cond:
    
    savings = 0 
    annual_salary = st_annual_salary
    for i in range(time):
        savings = savings + (savings*r)/12 + (annual_salary/12)*(ps_guess/10000)
        if (i%6 == 0) and (i != 0):
            annual_salary += annual_salary*semi_ann_raise
        
    #print(savings)
    if ps_guess > 9500:
        print("Its not possible for you to pay downpayment in 36 months with this salary")
        possible = False
        break
    
    if abs(savings - total_cost*down_payment) >= epsilon:
        cond = True
    else:
        cond = False
        
    if savings < total_cost*down_payment:
        ps_low = ps_guess
    else:
        ps_high = ps_guess 
        
    ps_guess = (ps_low + ps_high)//2
    #print(ps_guess)
    itr += 1 
if possible:
    print("Number of guesses : {}".format(itr))
    print("Optimal Savings Rate: {}".format(ps_guess/10000))
