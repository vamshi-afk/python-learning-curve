# Design a class as described below:
# Class Name: Addition
# Method:
# Function Name: add
# Parameters: a (int), b (int)
# Return Type: int
# Static: Yes (Use the @staticmethod decorator)
# Task: Returns the sum of the values given as parameters.

class Addition:

    @staticmethod
    def add(a,b):
        return a+b
    
a = int(input('enter value of a:'))
b = int(input('enter value of b:'))

print(f'Sum of a and b is: {Addition.add(a,b)}')