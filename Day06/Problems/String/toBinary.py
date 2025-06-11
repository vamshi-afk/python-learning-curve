# Given a decimal number n (positive) in string format, compute its binary string equivalent and return it. 

def toBinary(n):
    if n==0:
        return '0'
    
    binary=''
    while n>0:
        binary= str(n%2)+binary
        n//=2
    return binary

n = int(input("Enter a number: "))
if n >= 0:
    print(f"The binary representation of {n} is: {toBinary(n)}")
else:
    print("Please enter a non-negative integer.")