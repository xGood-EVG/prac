a, b = eval(input())
res = [i for i in range(a // 2 + 1, b + 1, 2) if '3' not in str(i)]
print(res)
