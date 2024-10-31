from itertools import islice

def slide(seq, n):
    it = iter(seq)
    window = tuple(islice(it, n))
    
    while window:
        yield from window
        window = window[1:] + tuple(islice(it, 1))

# print(*list(slide(range(5), 3)))

# print(*list(slide(range(2, 10), 2)))

# print(*list(slide(range(13, 23), 4)))

import sys
exec(sys.stdin.read())