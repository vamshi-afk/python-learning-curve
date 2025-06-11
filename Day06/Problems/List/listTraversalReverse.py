# You are given a list that contains integers. You need to print the elements of the list with in reverse order with a space between them.

def listTraversalReverse(arr):
    for i in reversed(arr):
        print(i, end=' ')

arr = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
listTraversalReverse(arr)