def isint(f):
    def newfun(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError
        return f(*args)
    return newfun

@isint
def i(a, b, c):
    return a, b, c

print(i(1, 2, 3))
