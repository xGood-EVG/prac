class IsType:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, func):
        def wrapper(*args):
            if not all(isinstance(arg, self.typ) for arg in args):
                raise TypeError
            return func(*args)
        return wrapper
    
@IsType(float)
def f(a,b,c):
    return a + b + c

@IsType(int)
def i(a,b,c):
    return a, b, c

print(f(2.0, 2.5, 0.5))
print(i(1,2,3))