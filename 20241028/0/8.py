from itertools import product


print(*[f"{i}{j}" for i, j in list(product("abcdefgh", range(1, 9)))], sep = ", ")
