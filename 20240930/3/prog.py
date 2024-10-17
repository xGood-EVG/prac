m1 = []
m2 = []

m1.append(eval(input()))
n1 = len(m1[0])

while len(m1) < n1:
    s = input()
    m1.append(list(map(int, s.split(','))))

while len(m2) < n1:
    s = input()
    m2.append(list(map(int, s.split(','))))

if not (all(len(row) == len(m1) for row in m1) and
        all(len(row) == len(m2) for row in m2) and
        len(m1) == len(m2)):
    raise ValueError("Не квадратные")

n = len(m1)
res = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            res[i][j] += m1[i][k] * m2[k][j]

for i in res:
    print(*i, sep = ',')


