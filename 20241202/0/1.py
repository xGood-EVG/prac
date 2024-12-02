with open('file.txt', 'rb') as f:
    text = f.read()

with open('file.txt', 'wb') as f:
    f.write(text[len(text) // 2:] + text[:len(text) // 2])