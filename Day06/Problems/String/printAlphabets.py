# Given two char c1 and c2.  you need to print all the alphabet starting from c1 to c2 in a single line.

def alphabets(c1,c2):
    s=''
    for i in range(ord(c1),ord(c2)+1):
        s+=chr(i)
    print(' '.join(s))

c1 = str(input("Enter first character: "))
c2 = str(input("Enter second character: "))

if len(c1) == 1 and len(c2) == 1:
    alphabets(c1, c2)
else:
    print("Please enter single characters only.")