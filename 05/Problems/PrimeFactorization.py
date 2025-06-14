def prime_factorization(n):
    # For numbers less than or equal to 1, as they don't have prime factors
    if n <= 1:
        return
        
    # Handle factor 2: continuously divide by 2 until n is odd
    while n % 2 == 0:
        print(2, end=' ')
        n //= 2 # Update n integer division by 2
        
    # Initialize divisor to 3, as we've handled all factors of 2
    i = 3
    # Check for odd factors up to the square root of n
    while i * i <= n:
        while n % i == 0:
            print(i, end=' ')
            n //= i
        i += 2 # Move to the next odd number
        
    # If n is still greater than 1, it must be a prime factor itself
    if n > 1:
        print(n)

n = int(input())
prime_factorization(n)