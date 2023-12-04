height = int(input('Hi sara, gimme ur height pls:'))
weight = int(input('and gimme ur weight pls:'))

if height < 150:
    if weight < 40:
        print('thin')
    elif 40 <= weight <= 50:
        print('normal')
    elif weight > 50:
        print('fat:(')

elif 150 <= height <= 180:
    if weight < 50:
        print('thin')
    elif 50 <= weight <= 80:
        print('normal')
    elif weight >= 80:
        print('fat')
elif height > 180:
    if weight < 80:
        print('thin')
    elif 80 <= weight <= 90:
        print('normal')
    elif weight >= 90:
        print('fat')