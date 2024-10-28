from itertools import count

def sum():
    s_sum = 0
    i = 1
    while True:
        s_sum += 1 / (i * i)
        yield s_sum
        i += 1
