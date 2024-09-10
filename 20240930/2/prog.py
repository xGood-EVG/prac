x = list(map(int, input().split(',')))
n = len(x)
for i in range(n):
    for j in range(0, n - 1 -i):
        k1 = (x[j] ** 2) % 100
        k2 = (x[j+1] ** 2) % 100
        if k1 > k2:
            x[j], x[j+1] = x[j+1], x[j]

print(x)
