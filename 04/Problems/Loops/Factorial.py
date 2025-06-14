# Given an integer n, write a program to return the factorial of n. The Factorial of a number is the product of all the numbers from 1 to n.
n = int(input())

fact=1

for i in range(2,n+1):
    fact*=i
print(fact)