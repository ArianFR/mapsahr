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
new_dict = {key.replace("'", ''): value for key, value in inv_map.items()}

def convertj(mx):

    global new_dict
    sentence = ''

    splited_sen =mx.split(' ')

    for i in splited_sen:
        if i == '':
            sentence += ' '
        for j in new_dict:
            if j == i:
                j = new_dict[j]
                sentence += j




    return sentence

if any(char in jomle for char in ['.', '-']):
    converted = convertj(jomle)
    converted = converted.replace('    ', ' ')
    print(converted)
else:
    converted = convertm(jomle)
    print(''.join(converted).replace("'", ""))
