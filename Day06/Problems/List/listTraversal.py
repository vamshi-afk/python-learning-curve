# You are given a list that contains integers. You need to print the elements of the list with a space between them.
# Note: Do not add a new line at the end.

def listTraversal(arr):
    for i in arr:
        print(i, end=' ')

arr = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
listTraversal(arr)