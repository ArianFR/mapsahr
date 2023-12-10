jomle = input('Hey!, type ur sentence or morse code: ')

with open('dictionary.py', 'r') as of:

    morse_dict = {}

    for line in of:
        key, value = line.split('=')
        morse_dict[key.strip()] = value.strip()



def find_key(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def convertj(mx):
    mkv = ''
    jkv = ''

    global morse_dict

    splited_sen = mx.split('     ')

    for word in splited_sen:
        for char in word.split(' '):
            for code in morse_dict.values():
                if char == code:
                    jkv = find_key(morse_dict, code)
                    mkv += jkv
    print(mkv)


convertj(jomle)







