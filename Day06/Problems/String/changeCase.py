# Given a string s, you need to perform the following operation.

# 1. Capitalize the first letter and print in a new line.
# 2. Convert the whole string to uppercase and print in a new line.

def changeCase(s):
    return s.capitalize(), s.upper()
s= str(input("Enter a string: "))
capitalized, uppercased = changeCase(s)
print("Capitalized string is:", capitalized)
print("Uppercased string is:", uppercased)