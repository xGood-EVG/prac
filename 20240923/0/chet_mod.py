while s:= input():
    if (int(s)%2) == 0:
        print(int(s))
    if int(s) == 13:
        print("Found 13")
        break
else:
    print("Congrats!")
