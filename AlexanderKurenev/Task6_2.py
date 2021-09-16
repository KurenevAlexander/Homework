a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, d + 1):
    print('\t', j, sep='', end='')
print()
for i in range(a, b + 1):
    print(i, end='')
    for j in range(c, d + 1):
        print('\t', i * j, sep='', end='')
    print()
