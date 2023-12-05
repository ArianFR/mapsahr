k = int(input('hey, type ur key:'))
txt = input('type ur text:')
b = []
c = str()
def hash(x):
    global txt
    global k
    for i in txt:
        if ord(i) == 32 or ord(i) == 46:
            b.append(i)
        elif ord(i) + k < 65:
            i = chr(ord(i) + (25 - (-k-1)))
            b.append(i)
        elif ord(i) + k > 90:
            i = chr(ord(i) - (25 - (k-1)))
            b.append(i)
        else:
            i = chr(ord(i) + k)
            b.append(i)
    c = ''.join(b)
    return c

print(hash(txt))
