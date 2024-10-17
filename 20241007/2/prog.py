def subtract(a, b):
    if type(a) != type(b):
        return("Ошибка типов")  # Возвращаем None, если типы не совпадают

    if isinstance(a, (int, float)):
        return a - b

    if isinstance(a, (list, tuple)):
        return type(a)(item for item in a if item not in b)

<<<<<<< HEAD
    if isinstance(a, str): 
        return a.replace(b , '')
    
    return None

a, b = eval(input())
print(subtract(a, b))
=======
    return None

result1 = subtract(1000, 1234)
result2 = subtract(102341.12345, 4134.9755)
result3 = subtract((4,2,7,4,6,87,7), (2,54,67,3,2))
result4 = subtract(["Q", "WE", "RTY"], ["WE", "ZZ"])
result5 = subtract("qwerqwedasdg", 5)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
>>>>>>> f7e4e7c4a572a19379eb7d9366907d89bccf405a
