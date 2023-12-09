jomle = input('Hey!, type ur sentence: ')

with open('dictionary.py', 'r') as of:
    morse_dict = {}
    for line in of:
        key, value = line.split('=')
        morse_dict[key.strip()] = value.strip()
def convert(jx):
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

for i in jomle:
    if i != '.' or i != '-':
        converted = convert(jomle)

        print(''.join(converted).replace("'", ""))
    break



