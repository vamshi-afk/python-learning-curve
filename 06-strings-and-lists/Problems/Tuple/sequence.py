# You are given a tuple numbers that contains a A.P sequence integer. You need to calculate the next three sequences of numbers and return the whole sequence in a tuple.

def sequence(numbers):
    tup = list(tup)
    d=tup[1]-tup[0]
    
    a=tup[-1]    
    for _ in range(3): # for the next three terms
        a+=d
        tup.append(a)
    
    return tuple(tup)

tup = tuple(map(int, input("Enter the elements of the tuple separated by spaces: ").split()))
result = sequence(tup)
print(f"The next three terms in the sequence are: {result}")