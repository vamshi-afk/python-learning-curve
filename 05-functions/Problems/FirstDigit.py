# Given a number n, find the first digit of the number.
def firstDigit(n):
    while n>=10:
        n=n//10
    return n
n=int(input())
print(firstDigit(n))
