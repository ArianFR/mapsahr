import math
x = float(input('hey sara, pls gimme ur wished number:'))
n = int(input('how many terms?'))
d = []
def taylor_series_cos(x, n):
    result = 0.0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        if term >= 0:
            m = f"+{term}"
            d.append(m)
        else:
            d.append(term)
        result += term
    return result
    return d

result_cos = taylor_series_cos(x, n)

result_string = ' '.join(str(item) for item in d)

print(result_string)



