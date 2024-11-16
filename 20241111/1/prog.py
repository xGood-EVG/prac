class Omnibus:
    _global_counts = {}

    def __init__(self):
        self._attributes = set()

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            if name not in self._attributes:
                self._attributes.add(name)
                Omnibus._global_counts[name] = Omnibus._global_counts.get(name, 0) + 1

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(f"Атрибут {name} не найден")
        return Omnibus._global_counts.get(name, 0)

    def __delattr__(self, name):
        if name.startswith("_"):
            if name in self.__dict__:
                super().__delattr__(name)
        elif name in self._attributes:
            self._attributes.remove(name)
            Omnibus._global_counts[name] -= 1
            if Omnibus._global_counts[name] == 0:
                del Omnibus._global_counts[name]

import sys
exec(sys.stdin.read())