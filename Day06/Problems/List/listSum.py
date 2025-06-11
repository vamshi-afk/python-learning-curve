# You are given a list that contains integers. You need to return the sum of the list.

def listSum(arr):
    return sum(arr)

arr = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
result = listSum(arr)
print(f"The sum of the list is: {result}")