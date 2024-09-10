from math import sin, cos

def scale(a, b, A, B, x):
    return (x - a)*(B-A)/(b-a)+A

A, B = -4, 4

for i in range(20):
    x = scale(0, 19, A, B, i)
    y = sin(x)
    space = round(scale(-1, 1, 0, 40, y))
    print(space * " ", "▼")