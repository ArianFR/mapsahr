jamshit, farshit, mahshit, noshit = map(int, input('how many candy in each persons side?: ').split(" "))
nafarat = {'j': jamshit, 'f': farshit, 'm': mahshit, 'n': noshit}

def candy_thing(x):
    global nafarat

    for i in nafarat:
        i -= 1
