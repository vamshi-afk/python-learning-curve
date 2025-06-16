# You are given a list that contains integers. You need to return the length of the list.

def listLength(arr):
    return len(arr)

arr = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
result = listLength(arr)
print(f"The length of the list is: {result}")