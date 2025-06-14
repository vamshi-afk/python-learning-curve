# You are given a number k and a list arr that contains integers. You need to return list of numbers that are less than k.

def lessThan(arr, k):
    return [i for i in arr if i < k]

arr = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
k = int(input("Enter the value of k: "))
result = lessThan(arr, k)
print(f"The elements less than {k} are: {' '.join(map(str, result))}")