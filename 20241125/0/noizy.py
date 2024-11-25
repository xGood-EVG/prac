class Dsc:
    def __get__(self, obj, cls):
        print(f"Get from {cls}:{repr(obj)}")
        return obj.value

    def __set__(self, obj, val):
        print(f"Set in {repr(obj)} to {val}")
        obj.value = val

    def __delete__(self, obj):
        print(f"Delete from {repr(obj)}")
        obj.value = None

class C:
    data = Dsc()

    def __init__(self, name):
        self.data = name

    def __str__(self):
        return f"<{self.data}>"
