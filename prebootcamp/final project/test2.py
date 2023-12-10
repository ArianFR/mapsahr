jomle = input('Hey!, type ur sentence or morse code: ')

with open('dictionary.py', 'r') as of:
    morse_dict = {}
    for line in of:
        key, value = line.strip().split(' = ')
        morse_dict[value] = key

def convertj(mx):
    mkv = ''
    splited_sen = mx.split('     ')

    for i in splited_sen:
        splited_word = i.split(' ')
        for morse_code in splited_word:
            mkv += morse_dict.get(morse_code, '')  # get the character from the dictionary, default to '' if not found
        mkv += ' '  # add a space at the end of each word

    return mkv.strip()  # remove trailing spaces

print(convertj(jomle))