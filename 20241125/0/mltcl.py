def multicall(times):
    def decorator(fun):
        def newfun(*args):
            return [fun(*args) for i in range(times)]
        return newfun
    return decorator

@multicall(4)
def ffun(n):
    return n * 2 + 1

print(ffun(9))
