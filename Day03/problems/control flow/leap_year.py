# check if the given year is a leap year

year = int(input())

if (year%4==0 and year%100!=0) or year%400==0:
    print('True')
else:
    print('False')
    