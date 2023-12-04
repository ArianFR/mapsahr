a = str
b = str
c = str
d = str
e = str

rooz = int(input('hey hassan, pls gimme the day num:'))
air_condition = str(input("gimme that day's condition:"))

driveday_list = [1, 3, 5, 7]
gymday_list = [2, 4, 6]

noumbrelladay_list = ['b', 'c']
umbrelladay_list = ['a', 'd', 'e']

if rooz in driveday_list:

    if air_condition in umbrelladay_list:
        print('driving class with umbrella')

    elif air_condition in noumbrelladay_list:
        print('driving class without umbrella')

    else:
        print('wrong condition')

elif rooz in gymday_list:

    if air_condition in umbrelladay_list:
        print('gym with umbrella')

    elif air_condition in noumbrelladay_list:
        print('gym without umbrella')

    else:
        print('wrong condition')

else:
    print('wrong day')