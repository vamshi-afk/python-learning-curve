# Given a string s, you need to slice it so that the output is a substring that contains all the chracters except first and last.
# Note: The length of the s will be greater than 2.

def sliceString(s):
    if len(s) < 2:
        return "String is too short to slice"
    return s[1:len(s)-1]

s = str(input("Enter a string: "))
print("Sliced string is:", sliceString(s))