# Given two numbers a and b. The task is to find the GCD of  a and b.
# The GCD of two numbers is the largest number that can divide both a and b perfectly.

a = int(input())
b = int(input())

while b:
    a, b = b, a%b
print(a)

# This is a euclidean formula which is more efficient, i tend not to use python libraries when learning the logic