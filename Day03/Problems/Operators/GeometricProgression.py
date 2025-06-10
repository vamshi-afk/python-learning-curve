#A person receives a salary of 5000 rupees on 1st January 2020, and this salary doubles every year. We need to calculate the salary the person will receive on 1st January 2030.

a = 5000
r = 2
n = 11

nth_term = a*(r**(n-1)) #GP formula
print(nth_term)