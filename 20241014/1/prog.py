from fractions import Fraction

def equation(s, w, degree_A, coeff_A, degree_B, coeff_B):
    A = sum(Fraction(coeff_A[degree_A - i]) * s**i for i in range(degree_A + 1))
    B = sum(Fraction(coeff_B[degree_B - i]) * s**i for i in range(degree_B + 1))
    
    if B == 0:
        return False
    elif abs(A/B - Fraction(w)) < Fraction(1, 1000000):
        return True
    elif (A/B) != Fraction(w):
        return False

inpt = input().split(", ")
s = Fraction(inpt[0])
w = Fraction(inpt[1])
degree_A = int(inpt[2])
coeff_A = [Fraction(inpt[i]) for i in range(3, 3 + degree_A + 1)]
degree_B = int(inpt[4 + degree_A])
coeff_B = [Fraction(inpt[i]) for i in range(5 + degree_A, 5 + degree_A + degree_B + 1)]

# print(s, w, degree_A, coeff_A, degree_B, coeff_B)
print(equation(s, w, degree_A, coeff_A, degree_B, coeff_B))