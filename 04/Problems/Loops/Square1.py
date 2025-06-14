# Given an integer n, write a program to print the square of size n using "*" character. 

n = int(input())

#for hollow square
for i in range(n):
    if i==0 or i==n-1:
        for j in range(n):
            print('*', end=' ')
        print()
    else:
        for k in range(n):
            if k==0 or k==n-1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

print()

# For non-hollow square
for i in range(n):
    for j in range(n):
        print('*', end=' ')
    print()