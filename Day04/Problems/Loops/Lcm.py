# Given two numbers a and b. The task is to find out their LCM.

a = int(input())
b = int(input())
o_a =a # original a value
o_b =b # original b value

while b:
    a, b = b, a%b
    gcd = a

lcm = o_a*o_b//gcd
print(lcm)