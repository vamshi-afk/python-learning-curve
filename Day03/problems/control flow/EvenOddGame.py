# Given a number n, number of apples in a bag. You and your friend are picking one apple turnwise from the bag. It is given that the first attempt is always by you. The person picking the last apple will be the winner. 

# If you will win: print "You" (without quotes)
# If your friend will win: print "Friend" (without quotes)

n=int(input())

if n%2==0:
    print('Friend')
else:
    print('You')