h = []
x = str(input())
for a in x:
   h.append(a)
if h.count('R') >= 3 or (h.count('Y') >= 2 and h.count('R') >= 2) or h.count('G')  < 1:
    print("nakhor lite")
else:
    print('rahat baash')

