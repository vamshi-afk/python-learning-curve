# Given an integer n. Write a program to print the Right angle triangle wall. The length of perpendicular and base is n.  Use single loop and string multiplication.

n = int(input())
row = ('* ')

for i in range(1,n+1):
    print((row*i).rstrip())