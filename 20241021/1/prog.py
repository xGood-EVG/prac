from collections import defaultdict

n = input().lower()
pairs = defaultdict(set)

for i in range(len(n)-1):
    if n[i].isalpha() and n[i+1].isalpha():
        pairs[n[i]].add(n[i+1])

print(sum(len(v) for v in pairs.values()))
