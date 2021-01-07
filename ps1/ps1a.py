total_cost = float(input('Enter Total cost of your dream home : '))
annual_salary = float(input('Enter annual salary : '))
portion_saved = float(input('Enter percent of your salary to save, as decimal : '))
r = 0.04
portion_down_payment = 0.25
current_savings = 0
months = 0

while current_savings <= total_cost*portion_down_payment:
    current_savings = current_savings + (current_savings*r)/12 + (annual_salary/12)*portion_saved
    months += 1 
print(months)