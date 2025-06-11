# Given a string b representing a Binary Number, The problem is to find its decimal equivalent.

def binaryToDecimal(b):
    result = 0
    power = 1

    for bit in reversed(b):
        result += int(bit)*power
        power *=2

    return result # or can simply return int(b, 2)

b = input("Enter a binary number: ")
print(f"The decimal equivalent of binary {b} is: {binaryToDecimal(b)}")