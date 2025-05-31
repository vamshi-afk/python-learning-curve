# Given an integer n. Write a program to print all the divisors of n in a single line.
n = int(input())

divisors=set()

for i in range(1,int(n**0.5)+1):
    if n%i==0:
        divisors.add(i)
        divisors.add(n//i)
print(*sorted(divisors))

# *sorted() prints set without brackets, uses space between the values