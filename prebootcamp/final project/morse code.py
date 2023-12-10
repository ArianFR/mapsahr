jomle = input('Hey!, type ur sentence or morse code: ')

with open('dictionary.py', 'r') as of:

    morse_dict = {}

    for line in of:
        key, value = line.split('=')
        morse_dict[key.strip()] = value.strip()


def convertm(jx):

    morse_sen = []
    global morse_dict

    for jh in jx: #jh = jomle harf
        if ord(jh) == 32:
            morse_sen.append(morse_dict['space'])
        else:
            for harf in morse_dict:
                if jh == harf:
                    morse_sen.append(morse_dict[harf])
                    morse_sen.append(' ')

    return morse_sen


def fkv(dx, valx):
    kv = ''
    for key, value in dx.items():
        if value == valx:
            kv = kv + key
    return kv

def convertj(mx):

    global morse_dict

    splited_sen = list(mx.split('     '))
    splited = ''

    for i in splited_sen:
        splited_word = i.split(' ')

        for i in splited_word:
            for j in morse_dict.values():
                if ord(i) == 32:
                    continue
                else:
                    kv = fkv(morse_dict, j)
                mkv = mkv + kv











for i in jomle:

    if i != '.' or i != '-':
        converted = convertm(jomle)

        print(''.join(converted).replace("'", ""))
        break

    else:




