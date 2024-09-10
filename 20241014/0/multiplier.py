from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return(Type(x) * Type(y))

#x, y, Type = eval(input())

print(multiplier('1.2', '3.4', float))
print(multiplier('1.2', '3.4', Decimal))
print(multiplier("1/6", "2/3", Fraction))