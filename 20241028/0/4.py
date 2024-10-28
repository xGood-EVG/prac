def travel(n):
    while n > 0:
        yield "по кочкам"
        n -= 1
    return "и в яму"

def travelwrap(n):
    tmp = yield from travel(n)
    yield tmp

for i in travel(4):
    print(i)

print()

for i in travelwrap(3):
    print(i)
