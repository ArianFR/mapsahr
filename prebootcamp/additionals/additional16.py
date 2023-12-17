tedadharekat, fplace = map(str, input('hey!, type tedad harekat and the first place: ').split(' '))

def ffp(th, fp):
    x = int(th)
    roller = str(fp)
    while x > 0:
        x -= 1
        temp = input().split(' ')
        if roller in temp:
            temp.remove(roller)
            roller = temp[0]
    return roller


print(ffp(tedadharekat, fplace))
