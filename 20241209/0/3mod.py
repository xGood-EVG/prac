class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kw):
        if cls._instance is None:
             cls._instance = super().__call__(*args, **kw)
        return cls._instance

class S(metaclass=Singleton):
    A = 3
s, t = S(), S()
s.newfield = 100500
print(f"{s.newfield=}, {t.newfield=}")
print(f"{s is t=}")