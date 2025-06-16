# Implement a Python class ComplexNumber to demonstrate operator overloading for adding two complex numbers.

# Class Name: ComplexNumber

# Attributes:
# real (float): The real part of the complex number.
# imaginary (float): The imaginary part of the complex number.
# Constructor:
# __init__(self, real, imaginary): Initializes the real and imaginary attributes with the given values.
# Methods/Functions:

# __add__(self, other):
# Parameters: other (another ComplexNumber object)
# Task: Overload the + operator to add two complex numbers. The addition of two complex numbers (a + bi) and (c + di) is calculated as:
# Real part: a + c
# Imaginary part: b + d
# Return: A new ComplexNumber object representing the sum of the two complex numbers.

# __str__(self):
# Parameters: None
# Task: Overload the string representation of the object to return the complex number in the format "a + bi", where a is the real part and b is the imaginary part.

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real + other.real         # Add real parts
            imaginary_part = self.imaginary + other.imaginary  # Add imaginary parts
            return ComplexNumber(real_part, imaginary_part)
        return NotImplemented  # Let Python handle unsupported types

    def __str__(self):
        sign = '+' if self.imaginary >= 0 else '-'  # Handle sign of imaginary part
        return f'{self.real} {sign} {abs(self.imaginary)}i'

c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -2)

c3 = c1 + c2
print("First Complex Number: ", c1)
print("Second Complex Number:", c2)
print("Sum: ", c3)