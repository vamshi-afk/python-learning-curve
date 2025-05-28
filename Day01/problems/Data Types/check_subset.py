a = set(list(map(int, input('enter values of set a: ').split())))
b = set(list(map(int, input('enter values of set b: ').split())))

check_subset = a<=b

print(check_subset)