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



inv_map = {v: k for k, v in morse_dict.items()}

def convertj(mx):

    global inv_map
    sentence = []

    splited_sen =mx.split(' ')
    #splited_word = str(splited_sen.split(' ')).strip('[')
    splited = ''

    for i in splited_sen:
        for j in inv_map:
            for key, value in inv_map.items():
                if i == key:
                    sentence.append(value)

    return sentence


converted = convertj(jomle)
print(converted)


for i in jomle:

    if i != '.' or i != '-':
        converted = convertm(jomle)

        print(''.join(converted).replace("'", ""))
        break

    else:

        converted = convertj(jomle)

        print(converted)
        break




