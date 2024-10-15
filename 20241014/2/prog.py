from math import *

def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A

def screen(n):
    print('\n'.join(''.join(row) for row in n))

data = input().split()
W = int(data[0])
H = int(data[1])
A = float(data[2])
B = float(data[3])
func = data[4]

n = [[' '] * W for _ in range(H)]
ys = []
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = eval(func)
    ys.append(y)

min_y, max_y = min(ys), max(ys)

for i in range(W):
    y = ys[i]
    s = round(scale(min_y, max_y, 0, H - 1, y))
    n[H - s - 1][i] = '*'

screen(n)
