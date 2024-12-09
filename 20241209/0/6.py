import inspect


class C:
    a: int
    def __init__(self, x):
        if not isinstance(x, inspect.get_annotations(self.__class__)['a']):
            raise TypeError("Type is not same with annotation")    
        self.a = x

print(C(1).a)
print(C("1"))