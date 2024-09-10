from math import factorial
from decimal import Decimal, getcontext
from fractions import Fraction

def esum(N, one):
    res, fact = one, 1
    for i in range(1, N):
        fact *= i
        res += one/fact
    return res

getcontext().prec = 100
print(esum(18, 1))
print(esum(71, Decimal(1)))
print(esum(10, Fraction(1)))