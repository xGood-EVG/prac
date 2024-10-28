from collections import Counter

W = int(input())

lines = []
while (line := input()):
    lines.append(line)

text = ' '.join(lines).lower()
new = ''.join(char if char.isalpha() or char == ' ' else ' ' for char in text)
words = [word for word in new.split() if len(word) == W]
s_count = Counter(words)

s_words = sorted(word for word, count in s_count.items() if count == max(s_count.values()))
print(" ".join(s_words))
