def dumper(fun):
    def newfun(*args, **kwargs):
        print(">", args, kwargs)
        res = fun(*args, **kwargs)
        print("<", res)
        return res
    return newfun

@dumper
def f(a, b, c=3):
    e = a+b*c
    return e

res = f(3,4,5)
