st = set(map(int, input().split()))
i = int(input())
r = int(input())

st.add(i)
print(*sorted(st))

st.remove(r)
print(*sorted(st))

sum_value = sum(st)
print(sum_value)