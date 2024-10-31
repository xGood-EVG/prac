from itertools import product

print(*sorted(filter(lambda x: x.count("TOR") == 2, map("".join, product("TOR", repeat=int(input()))))), sep=", ")