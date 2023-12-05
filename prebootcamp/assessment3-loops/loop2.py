c = int()
b = []

while True:
    a = int(input('hey, pls gimme ur numbers:'))
    if a == -1:
        break
    a = str(a * 2)
    a = a[::-1]
    a = int(a)
    b.append(a)

for i in b:
    i = int(i)
    c = c + i

print(c)

