def divisor(a, b):
    try:
        if b < 3:
            raise ZeroDivisionError("Insufficient b!")
        return a / b
    except ZeroDivisionError as ex:
        return ex


print(divisor(12, 4))
print(divisor(3, 2))