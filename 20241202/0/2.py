with open('file.txt', 'r') as f:
    text = f.read()

    result = text[:len(text) // 3]
    i = len(text) // 3
    while i < len(text) and text[i] != '\n':
        result += text[i]
        i += 1

    print(result)