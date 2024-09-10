def MINF(f0, f1, f2):
    def fun(x):
        return(min(f0(x), f1(x), f2(x)))
    return fun
