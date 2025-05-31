# Given an integer n check if n is prime or not.
# A prime number is a number that is divisible by 1 and itself only.
# Note: Print "True" if n is prime, otherwise print "False".

n = int(input())

if n<=1:
    print('False')
else:
    is_prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            is_prime=False
            break
    print(is_prime)
         