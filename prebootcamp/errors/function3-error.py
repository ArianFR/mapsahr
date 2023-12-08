def prime_factors(number):
    factors = set()
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            factors.add(divisor)
            number = number // divisor
        else:
            divisor += 1

    x = 0
    for i in factors:
        x += int(i)

    return x

def digits_sum(number):
    number = str(number)
    y = int()
    for i in number:
        y += int(i)

    return y


def do_the_math(number):
    for i in range(number):
        p = int(prime_factors(i))
        d = int(digits_sum(i))
        pedar = int(i + p + d)
        if number == pedar:
            true_pedar = int(pedar)
            break
        else:
            continue
    try:
        return true_pedar
    except:
        bi_pedar = 'no'
        return bi_pedar








def fother_finder():
    t = 1
    while t > 0 :
        t = int(input('how many inputs?: '))
        t = t - 1
        input_number = int(input('gimme ur actual number: '))
        do_the_math(input_number)
        try:
            print('yes', pedar)
        except:
            print(bi_pedar)






fother_finder()