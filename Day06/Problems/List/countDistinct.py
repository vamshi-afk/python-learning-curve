# You are given a list arr that contains integers. You need to count distinct integers in list.

def countDistinct(arr):
    return len(set(arr))

arr = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
result = countDistinct(arr)
print(f"The count of distinct integers in the list is: {result}")