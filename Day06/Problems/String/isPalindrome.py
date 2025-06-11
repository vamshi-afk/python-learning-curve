def isPalindrome(s):
    s=s.lower()
    low = 0
    high = len(s)-1
    
    while low<high:
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    else:
        return True
s = str(input("Enter a string: "))
print("Is the string a palindrome?", isPalindrome(s))