# You are given a tuple numbers that contains integers. You need to return a tuple containing doubles of given numbers.

def doubleTup(numbers):
    return tuple(num * 2 for num in numbers)

numbers = tuple(map(int, input("Enter the elements of the tuple separated by spaces: ").split()))
result = doubleTup(numbers)
print(f"The tuple with doubled values is: {result}")