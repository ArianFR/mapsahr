c = int()
b = []

while True:
    a = int(input('hey, pls gimme ur numbers:'))
    if a == -1:
        break
    a = int(str(a * 2)[::-1])
    b.append(a)

for i in b:
    c = c + i

print(c)

