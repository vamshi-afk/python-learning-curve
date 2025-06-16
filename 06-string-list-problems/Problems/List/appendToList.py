# You are given three inputs a, b, c. You need to create a list and append a, b, c to the list and then return that list.

def appendToList(a,b,c):
    list=[]
    list.append(a)
    list.append(b)
    list.append(c)    
    return list

a = int(input("Enter the first element: "))
b = int(input("Enter the second element: "))
c = int(input("Enter the third element: "))
result = appendToList(a, b, c)
print(f"The list after appending the elements is: {result}")