# You are given a list arr that contains integers. You need to return average of the non negative integers.

def nonNegativeAverage(arr):
    non_negative_numbers = [num for num in arr if num >= 0]
    if not non_negative_numbers:
        return 0
    return sum(non_negative_numbers) / len(non_negative_numbers)

arr = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
result = nonNegativeAverage(arr)
print(f"The average of non-negative integers is: {result:.2f}")