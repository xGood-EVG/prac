def walk2d():
    x, y = 0, 0
    while True:
        dx, dy = yield(x, y)
        x, y = x + dx, y + dy

gen = walk2d()
print(next(gen))

# print(gen.send((1,2)))
# print(gen.send((-3,1)))
# print(gen.send((2,-3)))

from random import randint

while True:
    print(gen.send((randint(-5,5), randint(-5,5)))) # бесконечно куда-то идет :)
