from itertools import repeat

def repeater(seq, n):
    for i in seq:
        yield from repeat(i, n)
