from math import *

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

def screen(n):
    print('\n'.join(''.join(row) for row in n))

A, B = -5, 5
W, H = 60, 25
n = [[' '] * W for _ in range(H)]
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = sin(x)
    s = round(scale(-1, 1, 0, H - 1, y))
    n[s][i] = '*'

screen(n)