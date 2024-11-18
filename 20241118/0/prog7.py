while True:
    try:
        n = int(input())
    except Exception:
        print("Incorrect!")
    else:
        print("Finally")
        break
print(n)