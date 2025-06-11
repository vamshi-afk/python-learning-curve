# You are given a list numbers that contains integers. You need to return two lists, one of even numbers and other of odd numbers.

def evenOdd(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return even_numbers, odd_numbers

numbers = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
even_numbers, odd_numbers = evenOdd(numbers)
print(f"Even numbers: {' '.join(map(str, even_numbers))}")
print(f"Odd numbers: {' '.join(map(str, odd_numbers))}")