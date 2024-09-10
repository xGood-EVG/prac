def rbin(n, i):
    if i == 0:
        print(*n, sep="")
    else:
        rbin(n + [0], i - 1)
        rbin(n + [1], i - 1)

rbin([1], int(input()) - 1)
