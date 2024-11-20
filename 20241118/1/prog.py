import collections


class DivStr(collections.UserString):
    def __init__(self, stroka=""):
        super().__init__(stroka)

    def __floordiv__(self, other):
        length = len(self.data)
        return (DivStr(self.data[i * other:(i + 1) * other]) for i in range(length // other))
    
    def __mod__(self, n):
        rest = len(self)%n
        return self[-rest:] if rest else DivStr()
    
    def __add__(self, other):
        return DivStr(super().__add__(str(other)))


import sys
exec(sys.stdin.read())