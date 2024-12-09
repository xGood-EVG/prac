def func(self, obj):
    self.var = obj

C = type('C', (), {'var': 100500, '__init__': func})

print(C.var)
c = C(123)
print(c.var)