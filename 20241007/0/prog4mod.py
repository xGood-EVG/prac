def F(a,b):
    def fun(x):
        return a*x + c
    print(fun.__closure__)
    c = a + b
    return fun
