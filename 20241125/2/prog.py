class Num:
    
    def __get__(self, obj, cls):
        return getattr(obj, '_value', 0)

    def __set__(self, obj, value):
        if isinstance(value, (int, float)):
            obj._value = value
        elif hasattr(value, "__len__"):
            obj._value = len(value)
        else:
            raise TypeError("Unsupported type for Num")

from sys import stdin
exec(stdin.read())