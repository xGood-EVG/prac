matrix = []
transposed = []
while s := input():
    matrix.append(eval(s))
    transposed.append(eval(s))

if all(len(i) == len(matrix) for i in matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed[j][i]= matrix[i][j]


    res = transposed
    print(*res, sep="\n")
else:
    print("Не сработало")

