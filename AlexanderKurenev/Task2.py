d = {}
for ch in input().lower():
    d[ch] = d.get(ch, 0) + 1
print(d)
