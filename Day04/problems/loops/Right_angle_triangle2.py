n = int(input())

for i in range(n):
    if i==0:
        print('*')
    elif i == n - 1:
        print('* ' * n)
    else:
        print('*' + ' ' * (2 * i - 1) + '*')
        # the reason behinf 2*i-1 is if you check the o/p the space is a odd number increasing by 2 every line
        # so for example, when i=7(line8) it has 13 spaces in between when the n=9, which is 7*2-1=13