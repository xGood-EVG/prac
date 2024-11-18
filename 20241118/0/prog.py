class A:
    v = 1

class B(A):
    v = 2

b = B()
b.v = 3

print("До удаления", b.v)

del b.v
print("Удаление из b", b.v)

del B.v
print("Удаление из B", b.v)