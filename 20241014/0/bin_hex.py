#for i in range(12, 24):
 #   print(f"{bin(i):<8}" + '= ' f"{hex(i):>4}" for i in range(12, 24))


def bih(fr, to):
    mw = len(f"{to:b}{to:x}")
    for i in range(fr, to + 1):
        w = mw - len(f"{i:b}{i:x}")
        print(f"0b{i:b} = {' '* w}0x{i:x}")

bih(12, 23)
print("\n")
bih(23, 30)