# Given a string s, and a pattern p. You need to find if p exists in s or not and return the starting index of p in s. If p does not exist in s then -1 will be returned.
# Here p and s both are case-sensitive.

def findPattern(s,p):
    s=s.lower()
    return s.find(p)

s = str(input("Enter a string: "))
p = str(input("Enter a pattern to find: "))
print("Pattern found at index:", findPattern(s,p))