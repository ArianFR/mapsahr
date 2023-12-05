lvl = int(input('hey, pls gimme the game lvls:'))
a = 0
while a<lvl:
    a += 1
    if a % 5 == 0:
        print('HOP!')
    else:
        print(a)