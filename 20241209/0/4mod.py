res = eval(input())
match res:
    case 1, 2:
        print("Exact 1, 2")
    case a, 3:
        print(a, "with 3")
    case 2, *tail:
        print("2 with", tail)
    case _:
        print("No match, got ", res)