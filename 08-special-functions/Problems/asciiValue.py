# Given a character ch as input, print its ascii value.

ch = input('Enter a character: ')
if len(ch) == 1:
    ascii = ord(ch)
    print(f"ASCII of '{ch}' is {ascii}")
else:
    print("Please enter exactly one character.")

text = "Python"
ascii_values = [ord(char) for char in text]
print(ascii_values)