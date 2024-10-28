from itertools import filterfalse

n = int(input())
s = filterfalse(lambda x: x % n, range(21, 33))

print(*s)