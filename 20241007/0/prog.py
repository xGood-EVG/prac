def average(a, *args):
    s = sum((a,) + args)
    result = s / (1 + len(args))
    print(result)
