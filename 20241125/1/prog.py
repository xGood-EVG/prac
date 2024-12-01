def objcount(cls):
    class Wrapper(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            Wrapper.counter += 1
            super().__init__(*args, **kwargs)

        def __del__(self):
            Wrapper.counter -= 1
            if hasattr(super(), '__del__'):
                super().__del__()

    return Wrapper

from sys import stdin
exec(stdin.read())