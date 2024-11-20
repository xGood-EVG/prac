class Undead(Exception):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass

def necro(a):
    cases = {0: Skeleton, 1: Zombie, 2: Ghoul}
    raise cases[a % 3]
        
x, y = eval(input())
for i in range(x, y):
    try:
        necro(i)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Ghoul:
        print("Generic Undead")