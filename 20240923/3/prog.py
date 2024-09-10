N = int(input())

i = N
while i <= N + 2:
    j = N
    while j <= N + 2:
        prod = i * j
        total = 0
        tmp_prod = prod
        while tmp_prod > 0:
            total += tmp_prod % 10
            tmp_prod //= 10

        if total == 6:
            result = ":=)"
        else:
            result = str(prod)

        print(f"{i} * {j} = {result:<5}", end=' ')
        j += 1
    print()
    i += 1
