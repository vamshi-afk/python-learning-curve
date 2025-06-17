# You are given two integers a and b. Your task is to find the minimum value obtained from performing any of the following arithmetic operations between a and b: addition (+), subtraction (-), multiplication (*), and division (/).
# Make sure to use exception handling to manage any potential division by zero errors.
# Note: If division by zero is attempted, handle the exception and exclude the division operation from consideration.

def find_minimum(a, b):
    op_list = []
    op_list.append(a+b)
    op_list.append(a-b)
    op_list.append(a*b)
    try:
        op_list.append(a/b)
    except ZeroDivisionError:
        pass
    return min(op_list)

a = int(input('Enter a value:'))
b = int(input('Enter b value:'))

print(find_minimum(a, b))