a = int(input())
match a:
    case 1:
        print("ODIN")
    case 2:
        print("DWA")
    case 3:
        print("TRI")
    case chet if (chet%2) == 0:
        print("chet")
    case nechet:
        print(nechet, "-- это много")
