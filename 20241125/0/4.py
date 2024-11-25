class Counter:
    def __init__(self):
        self.counter = 0

    def __get__(self, obj, cls):
        return self.counter

    def __set__(self, obj, val):
        self.counter = val

class C:
    counter = Counter()
    def __init__(self):
        self.counter += 1
    def __del__(self):
        self.counter -= 1
