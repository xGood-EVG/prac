import inspect  


class dump(type):
    def __new__(metacls, name, parents, ns, **kwds):
        def wrap(func, name):
            def foo(self, *args, **kwargs):
                print(f'{name}: {tuple(args)}, {kwargs}')

                return func(self, *args, **kwargs)
            return foo

        for i in ns:
            if inspect.isfunction(ns[i]):
                ns[i] = wrap(ns[i], i)

        return super().__new__(metacls, name, parents, ns)

import sys
exec(sys.stdin.read())