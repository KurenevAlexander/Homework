n = int(input())
i = 1
out = []
while i * i <= n:
    if n % i == 0:
        out.append(i)
        if i != n // i:
            out.append(n // i)
    i += 1
out.sort()
print(out)
