class Vowel:
    __slots__ = ['a', 'o', 'u', 'i', 'e', 'y']

    def __init__(self, a=None, o=None, u=None, i=None, e=None, y=None):
        self.a = a
        self.o = o
        self.u = u
        self.i = i
        self.e = e
        self.y = y

    def __str__(self):
        values = []
        for letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            value = getattr(self, letter, None)
            if value is not None:
                values.append(f"{letter}: {value}")
        return ", ".join(values)

    @property
    def answer(self):
        return 42

    @property
    def full(self):
        return all(object.__getattribute__(self, letter) is not None for letter in ['a', 'e', 'i', 'o', 'u', 'y'])

    @full.setter
    def full(self, value):
        raise AttributeError("property 'full' is read-only")

    def __getattribute__(self, name):
        if name in Vowel.__slots__:
            value = object.__getattribute__(self, name)
            if value is None:
                raise AttributeError(f"no {name}")
            return value
        return object.__getattribute__(self, name)

from sys import stdin
exec(stdin.read())