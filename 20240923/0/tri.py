a, b, c = eval(input())
if a*b <= a*c + c*b and a*c <= b*c + b*a and b*c <= b*a + a*c and min(a, b, c) >0:
    print("TREUG")
else:
    print("NE TREUG")
