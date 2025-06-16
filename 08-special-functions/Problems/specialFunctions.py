# Given two lists of integers, perform the following operations:

# zip(): Combine both lists into one iterable of tuples.
# filter(): Filter out all elements in list1 that are greater than 2.
# map(): Multiply each element of list1 by 2 using a lambda function.

list1 = list(map(int, input('Enter elements of list1 seperated by spaces').split()))
list2 = list(map(int, input('Enter elements of list2 seperated by spaces').split()))

zipped = zip(list1, list2)
print(list(zipped))

filtered = filter(lambda x: x<=2, list1)
print(list(filtered))

mapped = map(lambda x: x*2, list1)
print(list(mapped))