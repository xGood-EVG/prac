def istype(typ):
    def decorator(fun):
        def wrapper(*args):
            if not all(isinstance(arg, typ) for arg in args):
                raise TypeError
            return fun(*args)
        return wrapper
    return decorator

@istype(float)
def sum(a, b, c=2):
    return a + b + c

print(sum(1.0, 2.25, 3.05))
print(sum(1,2,3))