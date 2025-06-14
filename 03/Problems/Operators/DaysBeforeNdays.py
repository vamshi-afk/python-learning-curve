# We’re also given a number n, which represents how many days before the starting day we want to go.
# Our task is to calculate the day that falls n days before the given day d.

d=0 #current day where 0=sunday
n=9 #no. of days before

days_before_n_days = (d-n)%7
print(days_before_n_days)