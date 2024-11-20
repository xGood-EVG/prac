class InvalidInput(Exception):
    pass


class BadTriangle(Exception):
    pass


def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except Exception:
        raise InvalidInput

    S = abs((x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)) / 2.0)
    if S <= 0:
        raise BadTriangle
    return S


while True:
    try:
        triag = triangleSquare(input())
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{triag:.2f}")
        break