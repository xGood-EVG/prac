text = "вопрос"
text = text.encode("cp1251")
print(text.decode("koi8-r"))

text = "бМХЛЮМХЕ"
text = text.encode("koi8-r")
print(text.decode("cp1251"))

text = "ОХРЮМХЕ"
text = text.encode("koi8-r")
print(text.decode("cp1251"))