# Given a dictionary, and a list of queries(keys), you have to find and print the value of each query from the dictionary if present else it prints "None".

a = list(map(int, input().split()))
b = list(map(str, input().split()))
query = list(map(int, input().split()))
dict = {}
for i in range(len(a)):
    dict[a[i]] = b[i]
        
ans = []
for key in query:
    val = dict.get(key, "None")
    ans.append(val)

print(*ans, sep='\n')
