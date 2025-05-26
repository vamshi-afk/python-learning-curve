#k key, v value: Insert given key k and value v in the dictionary, print 'Inserted' after inserting.
#d key: Delete the entry for a given key d and print 'Deleted' if the key to be deleted is present, else print '-1'.
#p key: Print marks of given key p in statement as "Marks of {student_name} is : {marks}". If key is not present print '-1'.

keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

my_dict[k]=int(v)
print('Inserted')

d = input()

if my_dict.pop(d, None) is not None:
    print('Deleted')
else:
    print(-1)

p = input()

if p in my_dict:
    print('Marks of {} is {}'.format(p,my_dict[p]))
else:
    print(-1)