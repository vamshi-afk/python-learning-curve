# Given an integer n,  write a program to print the square wall of size n using a single loop and string multiplication. 

n = int(input())

row = ('* '*n).rstrip()

for _ in range(n):
    print(row)