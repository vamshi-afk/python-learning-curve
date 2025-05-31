# Given an integer n. Write a program to find the first prime number greater than n.

n = int(input())

next_num=n+1

while True:
    if next_num<=1:
        next_num+=1
        continue
    for i in range(2,int(next_num**0.5)+1):
        if next_num%i==0:
            next_num+=1
            break
    else:
        print(next_num)
        break
    