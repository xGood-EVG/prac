def Pareto(*args):
    pareto = []
    for i in args:
        dom = False
        for j in args:
            if i != j:
                if j[0] >= i[0] and j[1] >= i[1] and (j[0] > i[0] or j[1] > i[1]):
                    dom = True
                    break
        if not dom:
            pareto.append(i)
    return tuple(pareto)

res = eval(input())
print(Pareto(*res))