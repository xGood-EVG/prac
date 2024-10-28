from itertools import dropwhile, islice

def sum():
    s_sum = 0
    i = 1
    while True:
        s_sum += 1 / (i * i)
        yield s_sum
        i += 1

gen = sum()
print(list(islice(dropwhile(lambda x: x <= 1.6, gen), 10)))

# for e in islice(dropwhile(lambda x: x <= 1.6, gen), 10):
#     print(e)