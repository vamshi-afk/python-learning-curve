# You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.

def decrementList(arr):
    return [x-1 for x in arr]

arr = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
result = decrementList(arr)
print(f"The decremented list is: {result}")