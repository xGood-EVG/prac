a = int(input())

if a % 2 == 0 and a % 25 == 0:
    x = "A +"
else:
    x = "A -"
if a % 2 != 0 and a % 25 == 0:
    y = "B +"
else:
    y = "B -"
if a % 8 == 0:
    z = "C +"
else:
    z = "C -"

print(*(x, y, z), sep=" ")
