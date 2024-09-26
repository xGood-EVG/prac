total_sum = 0
while total_sum <= 21:
    n = int(input())
    if n <= 0:
        print(n)
        break
    total_sum += n
else:
    print(total_sum)
