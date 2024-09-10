matrix = []
transposed = []
while s := input():
    matrix.append(eval(s))
    transposed.append(eval(s))

for i in range(len(matrix)):
    for j in range(len(matrix)):
        transposed[j][i]= matrix[i][j]


res = transposed
print(*res, sep="\n")

