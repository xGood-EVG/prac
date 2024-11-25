from string import ascii_letters

class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

class Slotter:
    __slots__ = tuple(ascii_letters)
    
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)
