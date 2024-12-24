def subtract(a, b):
    if type(a) != type(b):
        return("Ошибка типов")  # Возвращаем None, если типы не совпадают

    if isinstance(a, (int, float)):
        return a - b

    if isinstance(a, (list, tuple)):
        return type(a)(item for item in a if item not in b)

    if isinstance(a, str): 
        return a.replace(b , '')
    
    return None

a, b = eval(input())
print(subtract(a, b))
