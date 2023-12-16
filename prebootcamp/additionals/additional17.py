bedardnakhor = int(input('how many markers?: '))

color_list = list(map(int, input('colors: ').split(' ')))

def find_min_repeated_value(colors):
    ans_dict = {}
    for color in colors:
        ans_dict[color] = ans_dict.get(color, 0) + 1

    min_repeated = min(ans_dict.items(), key=lambda x: (x[1], x[0]))
    return min_repeated[0]

result = find_min_repeated_value(color_list)
print("The value with the minimum repetitions:", result)

#chatgpt used, need to study abt dict.get and lambda ...

